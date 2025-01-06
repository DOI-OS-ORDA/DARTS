import os

from django.test import TestCase
from unittest.mock import Mock
from search.operations.document_search import DocumentSearch
from search.operations.documents_import import DocumentsImport
from search.operations.text_conversion import TextConversion


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


class TextConversionTest(TestCase):

    def setUp(self):
        self.file_path = 'search/tests/fixtures/documents/Effects of a gasoline spill on hibernating bats.docx'
        self.filename = 'search/tests/fixtures/documents/Effects of a gasoline spill on hibernating bats.docx'
        self.expected_start_text = '![Description: USGS](media/image1.png)'
        self.subject = TextConversion


    def test_docx_from_filepath(self):
        actual_text = self.subject.from_filepath(self.file_path)
        self.assertTrue(actual_text.startswith(self.expected_start_text), msg=f"Expected '{self.expected_start_text}' but got '{str.join(" ", actual_text.split(" ")[:3])}'")


    def test_docx_from_file_bytes(self):
        with os.fdopen(os.open(self.file_path, os.O_RDONLY), 'rb') as fd:
            file_bytes = fd.read()
            actual_text = self.subject.from_file_bytes(self.filename, file_bytes)
            self.assertTrue(actual_text.startswith(self.expected_start_text), msg=f"Expected '{self.expected_start_text}' but got '{str.join(" ", actual_text.split(" ")[:3])}'")


    # def test_pdf_from_filepath(self):
    #     pass


    # def test_pdf_from_file_bytes(self):
    #     pass
