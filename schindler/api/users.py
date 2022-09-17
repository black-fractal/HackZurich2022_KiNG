import random

import names

from schindler.models import MAX_JOURNEY_FREQ, UserProfile, interests


def generate_random_users( number ):
    users = []        
    for item in range( number ):
        users.append( generate_random_user() )
    return users

def generate_random_user():
    user = UserProfile( name=names.get_full_name(), interests=random.choice( interests )[0], journey_frequency=random.randint(0, MAX_JOURNEY_FREQ) )
    user.save()
    return user
