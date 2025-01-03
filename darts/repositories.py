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
        # print(f"----> {doc}")
        doc.save()

    def search(self, query: str):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT
                filename,
                ts_rank_cd(search_text, query) AS rank,
                ts_headline(body, query, $$MaxFragments=2, MaxWords=20, MinWords=10, StartSel='<span class="highlight">', StopSel='</span>'$$) AS highlight
            FROM documents, websearch_to_tsquery(%s) query
            WHERE query @@ search_text
            ORDER BY rank DESC
            LIMIT 100;
        """, (query, ))
        self.conn.commit()
        for record in cur:
            print(record)

    def clear(self):
        # all().changeset("delete").commit()
        cur = self.conn.cursor()
        cur.execute(f"TRUNCATE documents")
        self.conn.commit()
