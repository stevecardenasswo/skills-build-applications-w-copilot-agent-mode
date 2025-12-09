from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc')
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel')

        # Activities
        Activity.objects.create(user='Iron Man', type='run', duration=30)
        Activity.objects.create(user='Batman', type='cycle', duration=45)
        Activity.objects.create(user='Wonder Woman', type='swim', duration=60)
        Activity.objects.create(user='Spider-Man', type='climb', duration=25)

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=120)
        Leaderboard.objects.create(team='dc', points=110)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Squats', description='Do 30 squats')
        Workout.objects.create(name='Running', description='Run for 15 minutes')

        # Ensure unique index on email
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
