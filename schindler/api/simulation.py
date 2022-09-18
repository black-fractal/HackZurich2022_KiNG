import random

from schindler.models import (MAX_JOURNEY_FREQ, Simulation, UserProfile,
                              interests)


def generate_random_simulation(number):
    simulation = []
    for _ in range(number):
        try:
            simulation.append(generate_random_request())
        except Exception as e:
            print(e)

    return simulation


def generate_random_request():
    delay = random.randint(0, 20)
    while True:
        src = random.randint(-1, 10)
        dst = random.randint(-1, 10)
        if src != dst:
            break

    user_ids = [user.id for user in UserProfile.objects.all()]
    user_request = Simulation(user_profile_id=random.choice(user_ids), source=src, destination=dst, delay=delay)
    user_request.save()
    return user_request.to_json()
