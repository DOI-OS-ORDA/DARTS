from django.test import TestCase
from django.http import HttpRequest
from search.views import search


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = search(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>Search • DARTS</title>", html)
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertTrue(html.endswith("</html>\n"))

    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>Search • DARTS</title>")
