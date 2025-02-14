from django.test import TestCase
from django.http import HttpRequest
from search.views import search

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>Search • DARTS</title>")
