from django.test import TestCase
from unittest.mock import Mock

from search.operations.document_view import DocumentView
from search.models import Document

class DocumentViewDocxTest(TestCase):

    def setUp(self):
        self.filename = 'search/tests/fixtures/documents/Effects of a gasoline spill on hibernating bats.docx'

        document = Document(
            body = "I assure you, we have data.",
            file = str.encode("I assure you, we have data."),
            filename = self.filename,
            filename_normal = self.filename,
            title = "Effects of a Gasoline Spill",
        )
        self.repo = Mock()
        self.repo.objects.get.return_value = document
        self.subject = DocumentView(self.filename, self.repo)


    def test_when_docx_returns_buffer(self):
        buffer, _filename, _mimetype = self.subject.call()
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_when_docx_returns_filename(self):
        _buffer, filename, _mimetype = self.subject.call()
        self.assertEqual(self.filename, filename)

    def test_when_docx_returns_mimetype(self):
        _buffer, _filename, mimetype = self.subject.call()
        docx_mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        self.assertEqual(docx_mimetype, mimetype)


class DocumentViewPdfTest(TestCase):

    def setUp(self):
        self.filename = 'search/tests/fixtures/documents/AssessmentPlanandRes_20000721.pdf'

        document = Document(
            body = "I assure you, we have data.",
            file = str.encode("I assure you, we have data."),
            filename = self.filename,
            filename_normal = self.filename,
            title = "Assessment Plan and Restoration",
        )
        self.repo = Mock()
        self.repo.objects.get.return_value = document
        self.subject = DocumentView(self.filename, self.repo)


    def test_when_pdf_returns_buffer(self):
        buffer, _filename, _mimetype = self.subject.call()
        self.assertGreater(buffer.getbuffer().nbytes, 0)

    def test_when_pdf_returns_filename(self):
        _buffer, filename, _mimetype = self.subject.call()
        self.assertEqual(self.filename, filename)

    def test_when_pdf_returns_mimetype(self):
        _buffer, _filename, mimetype = self.subject.call()
        self.assertEqual('application/pdf', mimetype)
