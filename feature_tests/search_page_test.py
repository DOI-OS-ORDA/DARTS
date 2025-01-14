import re
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from search.operations.documents_import import DocumentsImport
from .base import FeatureTest

class SearchTest(FeatureTest):

    def setUp(self):
        super().setUp()
        documents_folder = "search/tests/fixtures/documents/*"
        DocumentsImport(documents_folder).call()

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
