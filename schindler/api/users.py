import random

import names

from schindler.models import MAX_JOURNEY_FREQ, Cluster, UserProfile, interests
from schindler.ML.inference import predict_cluster



def generate_random_users(number):
    users = []
    for _ in range(number):
        try:
            users.append(generate_random_user())
        except Exception as e:
            print(e)

    return users


def generate_random_user():
    user_interests = ','.join([interest for interest, _ in random.sample(interests, random.randint(1, 7))])
    user = UserProfile(name=names.get_full_name(), journey_frequency=random.randint(0, MAX_JOURNEY_FREQ),
                       interests=user_interests, Cluster=calculate_cluster( user_interests ))
    user.interests = user_interests
    user.cluster = predict_cluster([user_interests])

    user.save()
    return user.to_json()

def calculate_cluster( list_of_interests ):
    pass