from search.relations.relation import Relation
from django.db import connection

class SearchResultsRelation(Relation):

    def call(self, *args):
        self.args = args
        query = args[0]
        offset = self.fetch_arg(1, 0)
        limit = self.fetch_arg(2, 20)

        sql_query = """
            SELECT
              id,
              filename,
              title,
              public,
              ts_rank_cd(search_text, query) AS rank,
              ts_headline(
                body,
                query,
                $$MaxFragments=0, MaxWords=40, MinWords=30, StartSel='<span class="highlight">', StopSel='</span>'$$
              ) AS highlight
            FROM
                search_document,
                websearch_to_tsquery(%s) query
            WHERE query @@ search_text
            ORDER BY rank DESC, filename ASC
            LIMIT %s
            OFFSET %s;
            """
        data = (query, offset, limit)

        with connection.cursor() as cursor:
            cursor.execute(sql_query, data)
            return self.dictfetchall(cursor)
