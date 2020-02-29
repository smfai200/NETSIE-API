from django_seed import Seed

seeder = Seed.seeder()

from Bridger.models import *
from django.contrib.auth.models import User

seeder.add_entity(User, 10)
seeder.add_entity(Category, 10)
seeder.add_entity(Story, 10)
seeder.add_entity(Season, 10)
seeder.add_entity(Episode, 10)
seeder.add_entity(EpisodeReview, 10)

inserted_pks = seeder.execute()