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


from darts.operations import DocumentSearch, DocumentsImport


class CustomAssertions:
    def assertInOrder(self, array: list, earlyElement, laterElement):
        earlyIndex = array.index(earlyElement)
        laterIndex = array.index(laterElement)
        if not earlyIndex < laterIndex:
            raise AssertionError(f'Expected {earlyElement} to appear before {laterElement}, but {earlyElement} was at index {earlyIndex} and {laterElement} was at index {laterIndex}')


class OperationsDocumentSearchTest(TestCase, CustomAssertions):

    def setUpClass():
        documents_folder = "search/tests/fixtures/documents/*"
        DocumentsImport(documents_folder).call()


    def tearDownClass():
        # TODO: remove documents from the test database
        pass


    def setUp(self):
        self.search_term = "bats"
        self.search = DocumentSearch(self.search_term).call()
        self.basenames = list(map(lambda entry : entry['filename'].split("/")[-1], self.search.results()))


    def test_with_matching_documents_returns_matching_results(self):
        self.assertIn('Effects of a gasoline spill on hibernating bats.docx', self.basenames)


    def test_with_matching_documents_does_not_return_incorrect_results(self):
        self.assertNotIn('10163_Final RPEA Burgess 01 20 05.pdf', self.basenames)


    def test_with_matching_documents_ranks_matches_appropriately(self):
        self.assertInOrder(
            self.basenames,
            'Effects of a gasoline spill on hibernating bats.docx',
            'Preliminary Research Bats and NRDAR.docx'
        )

'''
  context "with no documents" do
    before { DocumentsRepository.clear }
    it "returns no results" do
      expect(subject.call).to be_empty
    end
  end
end
'''
