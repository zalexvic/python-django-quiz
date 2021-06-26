"""django_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from register import views as reg_views
from quiz import views as quiz_views

urlpatterns = [
    path('', quiz_views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('sign-up/', reg_views.sign_up, name='sign_up'),
    path('game/', quiz_views.play, name='game'),
    path('update-score/', quiz_views.update_score, name='update_score'),
    path('load-new-question/', quiz_views.load_new_question, name='load_new_question')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
