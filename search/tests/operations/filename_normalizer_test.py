from django.test import TestCase
from search.operations.filename_normalizer import FilenameNormalizer

class FilenameNormalizerTest(TestCase):

    def setUp(self):
        self.subject = FilenameNormalizer()


    def test_replaces_underscores_and_hyphens(self):
        filename = "1132_WA_Lower-Duwamish-River_RP_2013.pdf"
        expected = "1132 WA Lower Duwamish River RP 2013"
        actual = self.subject.call(filename)
        self.assertEqual(expected, actual)


    def test_handles_datelike_numbers(self):
        filename = "Effectsofagasolinesp_20141130 (1).docx"
        expected = "Effectsofagasolinesp 2014 11 30 (1)"
        actual = self.subject.call(filename)
        self.assertEqual(expected, actual)


    def test_handles_camelcase(self):
        filename = "PhaseIDamageAssessme_20090210"
        expected = "Phase I Damage Assessme 2009 02 10"
        actual = self.subject.call(filename)
        self.assertEqual(expected, actual)


    def test_handles_non_datelike_numbers(self):
        filename = "10454_Army Creek_Draft_RP_Amendment_040423 Trustee final.pdf"
        expected = "10454 Army Creek Draft RP Amendment 2023 04 04 Trustee final"
        actual = self.subject.call(filename)
        self.assertEqual(expected, actual)
