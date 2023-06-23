from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model


class LoginTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='John', password='s8M7dh6GmFc')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()
    
    def test_correct(self):
        user = authenticate(username='John', password='s8M7dh6GmFc')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_wrong_username(self):
        user = authenticate(username='Maria', password='s8M7dh6GmFc')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='John', password='369DGvgbvV7W')
        self.assertFalse(user is not None and user.is_authenticated)