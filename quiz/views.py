import redis
import requests

from random import shuffle

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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


@login_required
def load_new_question(request):
    if request.method == "GET":
        data = dict()

        question_data = requests.get(url=settings.TRIVIA_API_QUESTION_URL).json()

        data['question'] = question_data['results'][0]['question']
        data['category'] = question_data['results'][0]['category']
        data['difficulty'] = question_data['results'][0]['difficulty'].upper()
        data['correct_answer'] = question_data['results'][0]['correct_answer']

        answers = question_data['results'][0]['incorrect_answers']
        answers.append(data['correct_answer'])

        shuffle(answers)

        data['answers'] = [(ind + 1, answer) for ind, answer in enumerate(answers)]

        return JsonResponse(data=data)


@login_required
def update_score(request):
    if request.method == "POST":
        username = request.user.username
        score = int(request.POST.get('score'))
        redis_instance.zincrby('leaderboard', score, username)
    return redirect('/load-new-question')


@login_required
def play(request):
    context = dict()

    question_data = requests.get(url=settings.TRIVIA_API_QUESTION_URL).json()

    context['question'] = question_data['results'][0]['question']
    context['category'] = question_data['results'][0]['category']
    context['difficulty'] = question_data['results'][0]['difficulty'].upper()
    context['correct_answer'] = question_data['results'][0]['correct_answer']

    answers = question_data['results'][0]['incorrect_answers']
    answers.append(context['correct_answer'])

    shuffle(answers)

    context['answers'] = [(ind+1, answer) for ind, answer in enumerate(answers)]

    return render(request, 'quiz/play.html', context=context)
