import requests
import json
import websocket
import ssl
import asyncio

from schindler import pgw_uri, my_id


def lifts_info():
    url = f'https://{pgw_uri}/lift/'

    response = requests.get(url)

    if response.status_code == 200:
        lifts = json.loads(response.text)
        return lifts
    else:
        raise Exception('Could not fetch data')


def publish(source: int, destination: int):
    url = f'https://{pgw_uri}/publish/'
    try:
        response = requests.post(
            url,
            headers={'Content-Type': 'text/plain'},
            data=json.dumps({
                'asyncId': my_id, 'options':
                    {"destination":
                         {"destinationFloor": destination}
                     }, "target":
                    {"floor": source}
            }))
        if response.status_code == 202:
            return json.loads(response.text)['asyncId'] == my_id
    except:
        pass
    return False


# async def call_elevator(ws, message):
#     payload = {
#         "Method": "POST",
#         "asyncId": 2,
#         "Request-URI": "/publish/",
#         "body-json": {
#             "asyncId": "8c19718674",
#             "options": {
#                 "destination": {
#                     "destinationFloor": 7,
#                     "destinationZone": "Floor 7"
#                 }
#             },
#             "target": {
#                 "floor": 1
#             }
#         }
#     }
#
#     ws.send(json.dumps(payload))
#     print("request sent")
#
#     for message in ws:
#         print(f"< {message}")
#         if "\"state\":\"succeeded\"" in message:
#             print("elevator arrived at the destination")
#             break
#
#
# async def main():
#     ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
#     ws.connect("wss://hack2.myport.guide")
#
#     print("connection open")
#     await call_elevator(ws, "")
#     ws.close()
#     print("connection closed")
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
