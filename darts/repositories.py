import os
import psycopg

from search.models import Document

class DocumentsRepository:

    def __init__(self, schema = Document):
        self.schema = Document

    def add(self, filename: str, file, body: str):
        doc = Document(
            filename = filename,
            file = file,
            body = body
        )
<<<<<<< HEAD
=======
        # print(f"----> {doc}")
>>>>>>> 2faa331 (Unit tests cover much existing functionality)
        doc.save()

    def clear(self):
        cur = self.conn.cursor()
        cur.execute(f"TRUNCATE documents")
        self.conn.commit()
