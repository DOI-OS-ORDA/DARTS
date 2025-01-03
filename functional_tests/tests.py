import re
import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class SearchTest(LiveServerTestCase):
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

    def test_can_search(self):
        # A user visits the search page
        self.browser.get(self.live_server_url)

        # They see Search in the browser title
        self.assertIn("Search", self.browser.title)

        # They see a search field
        inputbox = self.browser.find_element(By.ID, "id_query")
        self.assertTrue(inputbox)

        # They search for bats
        inputbox.send_keys("bats")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # They see highlighted results containing the search term
        results = self.browser.find_elements(By.CLASS_NAME, "search-result")
        self.assertTrue(any(re.search('bats', result.text, re.I) for result in results))

        # They search for outside of Kentucky
        # inputbox.send_keys("bats -Kentucky")
        # TODO click submit
        # self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()
