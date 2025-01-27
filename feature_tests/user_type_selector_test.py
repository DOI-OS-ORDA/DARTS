from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from search.operations.documents_import import DocumentsImport
from .base import FeatureTest

class UserTypeSelectorTest(FeatureTest):

    def test_can_select(self):
        # A user visits the home page
        self.browser.get(self.live_server_url)

        # They see "Select user type" in the header
        user_type_selector = self.browser.find_element(By.ID, "user_type")
        self.assertTrue(user_type_selector)

        # They see all the user types (no cases or regions yet)
        for usertype in ("Guest user", "Staff", "Superuser", "Tech support", "Regional coordinator",):
            self.assertTrue(self.browser.find_element(By.PARTIAL_LINK_TEXT, usertype))

        # They select "guest user"
        superuser_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Superuser")
        superuser_link.click()

        # They visit the search page (redundant but want to test persistence)
        self.browser.get(self.live_server_url)
        # They see "guest user" in the menu bar
        user_type_selector = self.browser.find_element(By.ID, "user_type")
        self.assertEqual("Superuser", user_type_selector.text)
