from search.relations.relation import Relation
from django.db import connection

class SearchResultsRelation(Relation):

    def call(self, *args):
        query = args[0]

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
                [query]
            )
            return self.dictfetchall(cursor)

