from django.test import TestCase
from django.shortcuts import reverse


class blog_list_view(TestCase):
    def test_blog(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)

    def test_name_blog(self):
        response = self.client.get(reverse('posts_list_view'))
        self.assertEqual(response.status_code , 200)
