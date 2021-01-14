import random

from django_server.models import User


def run(*args):
    members = ['adela', 'aaron', 'aiden', 'andrew', 'calvin', 'dennis', 'irene', 'jay', 'jin', 'jun', 'kai', 'lena',
               'luffy', 'neody', 'randy', 'ryon', 'stephen']

    data = [(x, random.randint(1, 10)) for x in members]

    for name, level in data:
        User.objects.create(name=name, level=level)
