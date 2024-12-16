import datetime

from django.test import TestCase
from django.utils import timezone

class DartsTests(TestCase):
    def test_equal(self):
        self.assertEqual(True, True)
