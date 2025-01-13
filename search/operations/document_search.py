import glob
import os
import subprocess

from collections import namedtuple
from darts.repositories import DocumentsRepository

class DocumentSearch:

    def __init__(self, query: str):
        self.query = query
        self.result_data = []

    def results(self):
        if len(self.result_data) > 0:
            return self.result_data
        else:
            self.call()
            return self.result_data

    def dictfetchall(self, cursor):
        """
        Return all rows from a cursor as a dict.
        Assume the column names are unique.
        """
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

