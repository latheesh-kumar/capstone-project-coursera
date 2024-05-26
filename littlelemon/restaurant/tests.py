# Create your tests here.
from django.test import TestCase
from .models import *

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Id=1,name="Briyani", price=80, description="Vennila icecream", inventory=100)
        self.assertEqual(item, "Briyani")