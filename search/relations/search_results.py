from search.relations.relation import Relation
from django.db import connection

class SearchResultsRelation(Relation):

    def call(self, **kwargs):
        options = {}
        allowed_keys = {'query', 'offset', 'limit', 'permissions'}
        options.update((k, v) for k, v in kwargs.items() if k in allowed_keys)

        sql_query = """
            SELECT
              (CASE public WHEN 't' THEN id WHEN 'f' THEN NULL END) as id,
              (CASE public WHEN 't' THEN filename WHEN 'f' THEN NULL END) as filename,
              title,
              public,
              ts_rank_cd(search_text, query) AS rank,
              (CASE public
               WHEN 't' THEN preview
               WHEN 'f' THEN 'This document contains information that matches your search, but this document is internal to the case team. For viewing permission, please contact the team.'
               END) as highlight
            FROM
                search_document,
                websearch_to_tsquery(%s) query,
                ts_headline(
                    body,
                    query,
                    $$MaxFragments=0, MaxWords=40, MinWords=30, StartSel='<span class="highlight">', StopSel='</span>'$$
                ) preview
            WHERE query @@ search_text
            ORDER BY rank DESC
            LIMIT %s
            OFFSET %s;
            """
        data = (
            options.get('query'),
            options.get('limit', 20),
            options.get('offset', 0),
        )

        with connection.cursor() as cursor:
            cursor.execute(sql_query, data)
            return self.dictfetchall(cursor)
