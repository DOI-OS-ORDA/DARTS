import glob
import os
import subprocess

from collections import namedtuple
from django.db import connection
from .repositories import DocumentsRepository

class DocumentSearch:

    def call(self):
        with connection.cursor as cursor:
            cursor.execute(
                """
                SELECT
                  filename,
                  ts_rank_cd(search_text, query) AS rank,
                  ts_headline(body, query, $$MaxFragments=2, MaxWords=20, MinWords=10, StartSel='<span class="highlight">', StopSel='</span>'$$) AS highlight
                FROM documents, to_tsquery(%s) query
                WHERE query @@ search_text
                ORDER BY rank DESC
                LIMIT 100;
                """,
                [query]
            )
            return cursor.fetchall()

    def namedtuplefetchall(cursor):
        """
        Return all rows from a cursor as a namedtuple.
        Assume the column names are unique.
        """
        desc = cursor.description
        nt_result = namedtuple("Result", [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def dictfetchall(cursor):
        """
        Return all rows from a cursor as a dict.
        Assume the column names are unique.
        """
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


class TextConversion:

    @classmethod
    def call(cls, file_path):
        return subprocess.check_output(cls.command_text(file_path), shell=True).decode(encoding='utf-8')

    def command_text(file_path):
        base, ext = os.path.splitext(file_path)
        match ext:
            case ".docx":
                return f'pandoc -f docx -t markdown "{file_path}"'
            case ".pdf":
                return f'pdftotext "{file_path}" -'


class DocumentImport:

    # @inject
    # def __init__(self, file_path: str, repository = Provide["repo.documents"], converter = ["ops.text"]):
    def __init__(self, file_path: str, repository = DocumentsRepository(), converter = TextConversion):
        self.file_path = file_path
        self.repository = repository
        self.text_converter = converter

    def call(self) -> None:
        self.repository.add(
            filename = self.file_path,
            file = open(self.file_path, "rb").read(),
            body = self.text_converter.call(self.file_path)
        )


# To do: DI the repository and config file path
# make "repo.documents" a factory
# def __init__(self, folder_path: str = Provide["config.documents_pattern"], repository = Provide["repo.documents"]):
class DocumentsImport:
    def __init__(self, folder_path: str = './darts/docs/*', repository = DocumentsRepository()):
        self.folder_path = folder_path
        self.repository = repository

    def call(self):
        filepaths = glob.glob(self.folder_path)
        for path in filepaths:
            DocumentImport(path, self.repository).call()


