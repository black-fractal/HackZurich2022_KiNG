from django.db import models

# Create your models here.

MAX_JOURNEY_FREQ = 1000

interests = [
    ('movie', 'Movies, Actors, Directors, Genres, ...'),
    ('science', 'Physics, Biology, Chemistry, Zoology, Astronomy, Medicine, Astrophysics, Earth Sciences, ...'),
    ('culture', 'Arts, Society, Philosophy, ...'),
    ('sports', 'Football, Basketball, Soccer, Tennis, ...'),
    ('food', 'Vegetables, Fruits, Grains, Beans, Nuts, Meat, Poultry, Seafood, Dairy, ...'),
    ('fashion', 'Vintage, Artsy, Casual, Grunge style clothing, Chic, Bohemian, Sexy, Exotic, ...'),
    ('pets', 'Cats, Dogs, Birds, Rabbits, Horses, Ferrets, Fish, ...'),
    ('joke', 'Observational, Anecdotal, Situational, Character, One-liner, Ironic, Deadpan, Farcical, Self-deprecating, Slapstick, ...'),
    ('politics', 'Band society, Chiefdom, Empires, Leagues, ...'),
    ('adventure', 'Yoga, Trekking, Cycling, Canoeing, Kayaking, Rock climbing, Multi-adventure travel, New Zealand, ...')
]


class Cluster(models.Model):
    name = models.CharField(max_length=64, null=True)


class UserProfile(models.Model):
    name = models.CharField(max_length=64)
    interests = models.TextField()
    journey_frequency = models.IntegerField()
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name='UserProfileCluster', null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'interests': self.interests,
            'journey_frequency': self.journey_frequency,
            'cluster': self.cluster,
        }

    def get_interests_list(self):
        return self.interests.split(',')

class Simulation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='SimulationUserProfile', null=True)
    source = models.IntegerField()
    destination = models.IntegerField()
    delay = models.PositiveIntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'user_profile': self.user_profile,
            'source': self.source,
            'destination': self.destination,
            'delay': self.delay,
        }
