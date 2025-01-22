from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from search.operations.documents_import import DocumentsImport
from .base import FeatureTest

class UserTypeSelectorTest(FeatureTest):

    def test_can_select(self):
        pass
        # A user visits the home page
        # self.browser.get(self.live_server_url)

        # They see Select user type in the browser title
        # self.assertIn("Search", self.browser.title)

        # They see all the user types (no regions yet)

        # They select "guest user"

        # They visit the search page (redundant but want to test persistence)
        # They see "guest user" in the menu bar

        # They see a search box
        # inputbox = self.browser.find_element(By.ID, "id_query")
        # self.assertTrue(inputbox)

        # They search for bats
        # inputbox.send_keys("bats")
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # They only see public results

        # They see highlighted results containing the search term
        # results = self.browser.find_elements(By.CLASS_NAME, "search-result")
        # self.assertTrue(any(re.search('bats', result.text, re.I) for result in results))
