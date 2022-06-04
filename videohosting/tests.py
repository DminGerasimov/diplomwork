from django.test import TestCase, Client
from videohosting import models
from django.contrib.auth.models import User as DjangoUser

class ViewsTestCase(TestCase):
    c = Client()

    @staticmethod
    def create_fixtures():
        # Create test user
        dj_user = DjangoUser.objects.create_user('test_name', 'test@test.test','test_password')
        dj_user.save()

        # Create all models
        user = models.User(name='UserName', surname='UserSurname')
        user.save()

    def test_api_available(self):
        # Availability of API
        response = self.c.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_user_list_available(self):
        # Avilability of User model loading, filtering by name & test user authenticating 
        self.create_fixtures()
        self.c.login(username='test_name', password='test_password')

        response = self.c.get(
            '/api/users/',
            {'username': 'UserName'},
        )
        self.assertEqual(response.status_code, 200)