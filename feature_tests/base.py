import re
import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class FeatureTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'/usr/bin/firefox-esr'
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        from selenium.webdriver.firefox.service import Service
        service = Service('/usr/local/bin/geckodriver')
        self.browser = webdriver.Firefox(options=options, service=service)

    def tearDown(self):
        self.browser.quit()
