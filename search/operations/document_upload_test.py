from django.test import TestCase

from search.operations.document_upload import DocumentUpload

class DocumentUploadTest(TestCase):

    def setUp(self):
        self.filename = 'search/tests/fixtures/documents/Effects of a gasoline spill on hibernating bats.docx'
        self.subject = DocumentUpload(self.file, self.title, self.repo)


    def test_when_valid_document_creates_record(self):
        self.fail("Not yet implemented")


    def test_when_invalid_document_returns_error(self):
        self.fail("Not yet implemented")

