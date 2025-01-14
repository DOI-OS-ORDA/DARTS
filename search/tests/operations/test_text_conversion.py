import os

from django.test import TestCase

from search.operations.text_conversion import TextConversion

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
