import glob
import os
import subprocess

from collections import namedtuple
from django.db import connection
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

    def call(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                  id,
                  filename,
                  ts_rank_cd(search_text, query) AS rank,
                  ts_headline(body, query, $$MaxFragments=2, MaxWords=20, MinWords=10, StartSel='<span class="highlight">', StopSel='</span>'$$) AS highlight
                FROM search_document, websearch_to_tsquery(%s) query
                WHERE query @@ search_text
                ORDER BY rank DESC, filename ASC
                LIMIT 100;
                """,
                [self.query]
            )
            self.result_data = self.dictfetchall(cursor)
            return self

    def namedtuplefetchall(self, cursor):
        """
        Return all rows from a cursor as a namedtuple.
        Assume the column names are unique.
        """
        desc = cursor.description
        nt_result = namedtuple("Result", [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def dictfetchall(self, cursor):
        """
        Return all rows from a cursor as a dict.
        Assume the column names are unique.
        """
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

