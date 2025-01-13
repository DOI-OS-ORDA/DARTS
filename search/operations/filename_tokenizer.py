class FilenameTokenizer:

    @staticmethod
    def call(self, filename):
        # in: 1132_WA_Lower-Duwamish-River_RP_2013.pdf
        # out: 1132 WA Lower Duwamish River RP 2013

        # in: 10454_Army Creek_Draft_RP_Amendment_040423 Trustee final.pdf
        # out: 10454 Army Creek Draft RP Amendment 04 04 23 Trustee final

        # in: Effectsofagasolinesp_20141130 (1).docx
        # out: Effectsofagasolinesp 2014 11 30

        # in: PhaseIDamageAssessme_20090210
        # out: Phase I Damage Assessme 2009 02 10
