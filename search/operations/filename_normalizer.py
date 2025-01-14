import re

class FilenameNormalizer:

    @staticmethod
    def call(filename):
        return re.sub('-', ' ', filename)
        # map-reduce calling all the steps on the input?


    def steps(self):
        (replace_hyphens)


    def replace_hyphens(input):
        pass
        # Ruby: input.gsub(/-/, '')
