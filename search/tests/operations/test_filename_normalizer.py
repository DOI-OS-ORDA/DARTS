from django.test import TestCase

class FilenameNormalizerTest(TestCase):

    def setUp(self):
        self.subject = FilenameNormalizer

    def test_replaces_underscores_and_hyphens(self):
        filename = "1132_WA_Lower-Duwamish-River_RP_2013.pdf"
        expected = "1132 WA Lower Duwamish River RP 2013"
        actual = subject.call(filename)
        assertEqual(expected, actual)

        # filename = "10454_Army Creek_Draft_RP_Amendment_040423 Trustee final.pdf"
        # expected = "10454 Army Creek Draft RP Amendment 04 04 23 Trustee final"
        # actual = subject.call(filename)

        # filename = "Effectsofagasolinesp_20141130 (1).docx"
        # expected = "Effectsofagasolinesp 2014 11 30"
        # actual = subject.call(filename)

        # filename = "PhaseIDamageAssessme_20090210"
        # expected = "Phase I Damage Assessme 2009 02 10"
        # actual = subject.call(filename)
