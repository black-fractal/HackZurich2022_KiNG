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
    while True:
        src = random.randint(-1, 11)
        dst = random.randint(-1, 11)
        if src != dst:
            break
    user_request = Simulation( user_profile=random.choice( sorted( UserProfile.objects.all() ) ), source=src, destination=dst, delay=random.randint(0, 30) )    
    user_request.save()
    return user_request.to_json()
