from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is succesfull"""
        email = 'test@test.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = "test@TesT.com"
        user = get_user_model().objects.create_user(email, '14141414')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email trhows error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1312412')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password='123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
