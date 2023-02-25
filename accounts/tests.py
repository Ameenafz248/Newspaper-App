from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.

class SignUpPageTests(TestCase):
    def test_by_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")


    def test_signup_create(self):
        response = self.client.post(reverse("signup"), {
            "username" : "testuser",
            "email" : "testuser@test.com",
            "password1" : "SuperStar123",
            "password2" : "SuperStar123",
            "age" : 45,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count() , 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@test.com")
