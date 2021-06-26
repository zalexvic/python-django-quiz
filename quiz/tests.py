from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class TestQuiz(TestCase):

    def setUp(self):
        self.index_url = reverse('index')
        self.sign_up_url = reverse('sign_up')
        self.game_url = reverse('game')
        self.update_score_url = reverse('update_score')
        self.load_new_question_url = reverse('load_new_question')

        self.user = User.objects.create_user(
            username='user',
            password='password'
        )

        self.client.force_login(self.user)

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_play_GET(self):
        response = self.client.get(self.game_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/play.html')

    def test_update_score_POST(self):
        response = self.client.post(self.update_score_url, {
            'score': 10
        })

        self.assertEquals(response.status_code, 302)

    def test_load_new_question_GET(self):
        response = self.client.get(self.load_new_question_url)

        self.assertEquals(response.status_code, 200)

    def test_sign_up_POST(self):
        response = self.client.post(self.sign_up_url, {
            'username': 'testuser1',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.get(username='testuser1').username, 'testuser1')
