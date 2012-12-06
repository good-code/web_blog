from django.test.client import Client
from django.utils import unittest
from models import Post

class Goodcode_test(unittest.TestCase):
   def setUp(self):
      self.c = Client()

   def test(self):
      response = self.c.get('/')
      self.assertEqual(response.status_code, 200)

   def test2(self):
      for post in Post.objects.filter(active=True):
	 response = self.c.get('/post/%s' % post.sku)
	 self.assertEqual(response.status_code, 200)
