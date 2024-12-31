import glob
import os
import psycopg
import subprocess


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
    def __init__(self, file_path: str, repository, converter = TextConversion):
        self.file_path = file_path
        self.repository = repository
        self.text_converter = converter

    def call(self):
        self.repository.add(
            filename = self.file_path,
            file = open(self.file_path, "rb").read(),
            body = self.text_converter.call(self.file_path)
        )


class DocumentsImport:
    def __init__(self, folder_path: str = './darts/docs/*', repository_class = DocumentsRepository):
        self.folder_path = folder_path
        self.repository = repository_class()

    def call(self):
        filepaths = glob.glob(self.folder_path)
        for path in filepaths:
            DocumentImport(path, self.repository).call()


DocumentsImport().call()


# cur.execute("""
#     CREATE TABLE IF NOT EXISTS documents (
#       filename varchar(255),
#       file bytea,
#       body text,
#       search_text tsvector GENERATED ALWAYS AS (to_tsvector('english', coalesce(filename, '') || ' ' || coalesce(body, ''))) STORED
#     );
# """)
