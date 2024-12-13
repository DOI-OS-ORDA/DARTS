import os
from os import listdir

filepaths = os.listdir('./darts/docs/')

for path in filepaths:
    base, ext = os.path.splitext(path)
    match ext:
        case ".docx":
            subprocess.check_output(f'pandoc -f docx -t markdown "darts/docs/{path}"', shell=True)
        case ".pdf":
            subprocess.check_output(f'pdftotext "darts/docs/{path}" -', shell=True)

import psycopg
conn = psycopg.connect("dbname=postgres user=postgres")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
      filename varchar(255),
      file bytea,
      body text,
      search_text tsvector GENERATED ALWAYS AS (to_tsvector('english', coalesce(filename, '') || ' ' || coalesce(body, ''))) STORED
    );
""")

cur.execute("""
    INSERT INTO documents (filename, body)
    VALUES ('a_pdf_about_bats.pdf', 'this is a story about bats')
""")

conn.commit

cur.execute("""
    SELECT * FROM documents
    WHERE search_text @@ to_tsquery('bat')
""")

for record in cur:
    print(record)
