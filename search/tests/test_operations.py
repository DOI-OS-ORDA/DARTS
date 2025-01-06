from django.test import TestCase
from unittest.mock import Mock
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

    def test_with_no_documents_returns_no_results(self):
        self.fail("""
            This test is showing a design weakness. There's no way to inject
            the repository for document search because it's hardcoded SQL.

            This should head in the direction of:
                - Search operation
                - Repository that has a method for querying search results
                - Return results wrapped in a SearchResult struct
        """)
        empty_repo = Mock()
        empty_repo.results.return_value = []
        search = DocumentSearch(self.search_term).call()
        self.assertEqual(len(search.results()), 0)
