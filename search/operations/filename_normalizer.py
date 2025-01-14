import os
import re

from dateutil.parser import parse
from functools import reduce

class FilenameNormalizer:

    def call(self, filename):
        return reduce(
            lambda text, step : step(text),
            self.steps(),
            filename
        )


    def steps(self):
        return (
            lambda x : os.path.splitext(x)[0],             # Get file basename
            lambda x : re.sub('-', ' ', x),                # Replace dashes
            lambda x : re.sub('_', ' ', x),                # Replace underscores
            lambda x : self.split_date(x),                 # Format date
            lambda x : ' '.join(self.camel_case_split(x)), # Split camel casing
        )


    def split_date(self, text):
        date_pattern = "(\\d{6,8})" # possible date formats: 20240114 011424
        return ''.join(list(map(
            lambda maybeDate : parse(maybeDate).strftime('%Y %m %d') if re.match(date_pattern, maybeDate) else maybeDate,
            re.split(date_pattern, text)
        )))


    def camel_case_split(self, identifier):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
        return [m.group(0) for m in matches]
