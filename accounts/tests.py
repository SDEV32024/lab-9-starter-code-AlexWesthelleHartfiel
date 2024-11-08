from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
# Create your tests here.

class CustomeUserTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@t.com',
            password='tpassword',
            age=23
        )

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@t.com')
        self.assertEqual(self.user.age,23)
        self.assertTrue(self.user.check_password('tpassword'))

    def test_superuser_creation(self):
        self.superuser = get_user_model().objects.create_superuser(
            username='suser',
            email='suser@s.com',
            password='spassword',
            age=23
        )

        self.assertEqual(self.superuser.username, 'suser')
        self.assertEqual(self.superuser.email, 'suser@s.com')
        self.assertTrue(self.superuser.check_password('spassword'))
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='tpassword',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            date_of_birth='2001-12-12',
            fav_author = 'Archer',
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.date_of_birth, '2001-12-12')
        self.assertEqual(self.profile.fav_author, 'Archer')
    
    def test_profile_str_representation(self):
        expected_str = "testuser"
        self.assertEqual(str(self.profile), expected_str)
    
    def test_get_absolute_url_method(self):
        expected_str = '/accounts/profile/{}/'.format(self.profile.pk)
        self.assertEqual(self.profile.get_absolute_url(), expected_url)