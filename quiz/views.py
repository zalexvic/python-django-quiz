import redis

from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT,
                                   db=0)


# Create your views here.
def index(request):
    user = request.user
    context = dict()

    if user.is_authenticated:
        leaderboard = [(player.decode('utf-8'), score) for player, score in redis_instance.zrevrange('leaderboard', 0, -1, withscores=True)]
        players_per_page = 10

        paginator = Paginator(leaderboard, players_per_page)

        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)

        context = {'page': page}

    return render(request, 'quiz/index.html', context=context)