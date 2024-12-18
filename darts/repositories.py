import os
import psycopg

class DocumentsRepository:

    def __init__(self, connection_string: str = f'password={os.environ['POSTGRES_PASSWORD']} user={os.environ['POSTGRES_USER']} host=db'):
        self.conn = psycopg.connect(connection_string)

    def all(self, limit=100):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM documents LIMIT {limit}")
        self.conn.commit()
        for record in cur:
            print(record)

    def add(self, filename: str, file, body: str):
        # self.changeset("create", filename = filename, file = file, body = body).commit()
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO documents (filename, file, body)
            VALUES (%s, %s, %s)
            """,
            (filename, file, body)
        )
        self.conn.commit()

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
