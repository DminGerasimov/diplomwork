from django.test import TestCase, Client
from videohosting import models
from django.contrib.auth.models import User as DjangoUser


class ViewsTestCase(TestCase):
    c = Client()

    @staticmethod
    def create_fixtures():
        # Create test user in django.contrib.auth.models
        dj_user1 = DjangoUser.objects.create_user('test_name1', 'test@test.test1','test_password1')
        dj_user1.save()
        dj_user2 = DjangoUser.objects.create_user('test_name2', 'test1@test2.test2','test_password2')
        dj_user2.save()

        # Create all models
        user1 = models.User(name='UserName1', surname='UserSurname1', django_user=dj_user1)
        user1.save()
        user2 = models.User(name='UserName2', surname='UserSurname2', django_user=dj_user2)
        user2.save()

        subscription = models.Subscription()
        subscription.save()
        participant = models.Participant(subscription=subscription, user=user2, actor=user1)
        participant.save()
        subscription = models.Subscription()
        subscription.save()
        participant = models.Participant(subscription=subscription, user=user1, actor=user2)
        participant.save()

    def test_api_available(self):
        # Availability of API
        response = self.c.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_user_list_available(self):
        # Avilability of User model loading, filtering by name & test user authenticating 
        self.create_fixtures()
        self.c.login(username='test_name1', password='test_password1')

        # запрос всего списка
        response = self.c.get('/api/users/',)
        self.assertEqual(response.status_code, 200)

        # запрос с  фильтрацией
        response = self.c.get(
            '/api/users/',
            {'name': 'UserName1'},
        )
        self.assertEqual(response.status_code, 200)

    def test_participant_available(self):
        # Avilability of Participant model loading, 
        # filtering by 'subscription', 'user', 'actor' authenticating 
        self.create_fixtures()
        self.c.login(username='test_name1', password='test_password1')

        # запрос всего списка
        response = self.c.get('/api/participants/',)
        self.assertEqual(response.status_code, 200)

        # запрос с  фильтрацией
        response = self.c.get(
            '/api/participants/',
            {'actor': '1'},
        )
        self.assertEqual(response.status_code, 200)
