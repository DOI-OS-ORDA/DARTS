from django.test import TestCase

from search.operations.document_search import DocumentSearch
from search.operations.documents_import import DocumentsImport
from search.repositories.users import UsersRepository

class CustomAssertions:
    def assertInOrder(self, array: list, earlyElement, laterElement):
        earlyIndex = array.index(earlyElement)
        laterIndex = array.index(laterElement)
        if not earlyIndex < laterIndex:
            raise AssertionError(f'Expected {earlyElement} to appear before {laterElement}, but {earlyElement} was at index {earlyIndex} and {laterElement} was at index {laterIndex}')


class DocumentSearchTest(TestCase, CustomAssertions):

    def setUpClass():
        documents_folder = "search/tests/fixtures/documents/*"
        documents_metadata = "search/tests/fixtures/metadata.csv"
        DocumentsImport(documents_folder, documents_metadata).call()


    def tearDownClass():
        # TODO: remove documents from the test database
        pass


    def setUp(self):
        self.search_term = "bats"
        self.results = DocumentSearch(self.search_term).call()
        self.basenames = list(map(lambda entry : entry.filename.split("/")[-1], self.results))


    def test_with_matching_documents_returns_matching_results(self):
        self.assertIn('3_Effects of a gasoline spill on hibernating bats.docx', self.basenames)


    def test_with_matching_documents_does_not_return_incorrect_results(self):
        self.assertNotIn('1_Final RPEA Burgess 01 20 05.pdf', self.basenames)


    def test_with_matching_documents_ranks_matches_appropriately(self):
        self.assertInOrder(
            self.basenames,
            '3_Effects of a gasoline spill on hibernating bats.docx',
            '4_Preliminary Research Bats and NRDAR.docx'
        )

    # from unittest.mock import Mock
    # def test_with_no_documents_returns_no_results(self):
    #     self.fail("""
    #         This test is showing a design weakness. There's no way to inject
    #         the repository for document search because it's hardcoded SQL.

    #         This should head in the direction of:
    #             - Search operation
    #             - Repository that has a method for querying search results
    #             - Return results wrapped in a SearchResult struct
    #     """)
    #     empty_repo = Mock()
    #     empty_repo.results.return_value = []
    #     search = DocumentSearch(self.search_term).call()
    #     self.assertEqual(len(search.results()), 0)

class DocumentSearchAsGuestUserTest(TestCase):

    def setUpClass():
        documents_folder = "search/tests/fixtures/documents/*"
        documents_metadata = "search/tests/fixtures/metadata.csv"
        DocumentsImport(documents_folder, documents_metadata).call()


    def tearDownClass():
        # TODO: remove documents from the test database
        pass

    def setUp(self):
        self.search_term = "bats"
        self.known_private_title = "Restoration Plan Burgess Bats"
        self.subject = DocumentSearch(
            self.search_term,
            searcher = UsersRepository.get("guest")
        )
        self.results = self.subject.call()
        self.titles = list(map(lambda entry : entry.title, self.results))

    def test_guest_user_sees_only_public_results(self):
        self.assertNotIn(self.known_private_title, self.titles)


class DocumentSearchAsSuperuserTest(TestCase):
    def setUpClass():
        documents_folder = "search/tests/fixtures/documents/*"
        documents_metadata = "search/tests/fixtures/metadata.csv"
        DocumentsImport(documents_folder, documents_metadata).call()


    def tearDownClass():
        # TODO: remove documents from the test database
        pass

    def setUp(self):
        self.search_term = "bats"
        self.known_private_title = "Restoration Plan Burgess Bats"
        self.subject = DocumentSearch(
            self.search_term,
            searcher = UsersRepository.get("superuser"),
            searcher = None, # TODO Fill in
        self.assertIn(self.known_private_title, self.titles)
