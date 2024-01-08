from django.test import TestCase
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import UserSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username": "testcase", "email": "test@gmail.com", "password": "strong@1234"}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Neumann", password="Neumann007")
        self.token = Token.objects.create(user=self.user)
        self.user_authentication()

    def user_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_view_profile(self):
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_profile_unaunthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    class LoginTestCase(APITestCase):
        def setUp(self):
           self.user = User.objects.create_user(email="neumann@gmail.com", password="Neumann007")

        def test_login(self): 
            response = self.client.post("/api/users/login/")
            self.assertEqual(response.status_code, status.HTTP_200_OK) 
            

