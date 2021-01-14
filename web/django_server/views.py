import logging

from django.http import JsonResponse
from django.shortcuts import render

from django_server.models import User

logger = logging.getLogger(__name__)


# You have to run makemigrations and migrate before using this function.
def api(request):
    query = request.GET.get('query')
    logger.info(f'query: {query}')

    # user = User.objects.get(name__icontains=query)

    user = User.objects.first()
    data = {
        'name': user.name,
        'level': user.level,
    }
    return JsonResponse(data)


def index(request):
    data = {
        'name': 'Hello World',
        'users': User.objects.all()
    }
    return render(request, 'index.html', data)
