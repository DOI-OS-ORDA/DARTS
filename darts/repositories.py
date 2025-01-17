import os
import psycopg

from search.models import Document

class DocumentsRepository:

    def __init__(self, schema = Document):
        self.schema = Document

    def add(self, filename: str, file, body: str, title: str, public):
        doc = Document(
            filename = filename,
            file = file,
            body = body,
            title = title,
            public = public,
        )
        doc.save()

    def clear(self):
        cur = self.conn.cursor()
        cur.execute(f"TRUNCATE documents")
        self.conn.commit()
