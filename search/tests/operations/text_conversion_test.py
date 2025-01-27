import os

from django.test import TestCase

from search.operations.text_conversion import TextConversion

class TextConversionDocxTest(TestCase):

    def setUp(self):
        self.file_path = 'search/tests/fixtures/documents/3_Effects of a gasoline spill on hibernating bats.docx'
        self.filename = '3_Effects of a gasoline spill on hibernating bats.docx'
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


class TextConversionPdfTest(TestCase):
    def setUp(self):
        self.file_path = 'search/tests/fixtures/documents/1_Final RPEA Burgess 01 20 05.pdf'
        self.filename = '1_Final RPEA Burgess 01 20 05.pdf'
        # TODO I'd like better text to compare than this
        self.expected_start_text = ''
        self.subject = TextConversion


    def test_pdf_from_filepath(self):
        actual_text = self.subject.from_filepath(self.file_path).strip()
        self.assertTrue(actual_text.startswith(self.expected_start_text), msg=f"Expected '{self.expected_start_text}' but got '{str.join(" ", actual_text.split(" ")[:3])}'")


    def test_pdf_from_file_bytes(self):
        with os.fdopen(os.open(self.file_path, os.O_RDONLY), 'rb') as fd:
            file_bytes = fd.read()
            actual_text = self.subject.from_file_bytes(self.filename, file_bytes)
            self.assertTrue(actual_text.startswith(self.expected_start_text), msg=f"Expected '{self.expected_start_text}' but got '{str.join(" ", actual_text.split(" ")[:3])}'")

# TODO: 10164_Final RPEA Burgess ... is all empty, and that should throw an error of some sort
