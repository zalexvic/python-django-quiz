from django.conf import settings
from django.shortcuts import render, redirect
from .forms import RegisterForm
import redis

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT,
                                   db=0)


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            redis_instance.zadd('leaderboard', {form.cleaned_data['username']: 0})
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, 'register/signup.html', {'form': form})