import requests
import json

from schindler import pgw_uri


def lifts_info():
    url = f'https://{pgw_uri}/lift/'

    response = requests.get(url)

    if response == 200:
        lifts = json.loads(response.text)
        return lifts
    else:
        raise Exception('Could not fetch data')
