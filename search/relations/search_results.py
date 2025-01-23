from search.relations.relation import Relation
from django.db import connection

class SearchResultsRelation(Relation):

    def visibility_clause(self, perms):
        match perms:
            case 'hide':
                return ("AND public = 't'", None)
            case {'case_ids': case_ids}:
                print(f"----> CASE IDS {case_ids}")
                return ("AND cases.case_id IN %(ids)s", case_ids)
            case {'region_ids': region_ids}:
                print(f"----> REGION IDS {region_ids}")
                return ("AND cases.region_id IN %(ids)s", region_ids)
            case 'show':
                return ("AND (public = 'f' OR public = 't')", None)
            case _:
                return ("AND public = 't'", None)

    def can_see_private(self, perms):
        match perms:
            case 'hide':
                return 'f'
            case {'case_ids': case_ids}:
                return 't' # TODO with caveats
            case {'region_ids': region_ids}:
                return 't' # TODO with caveats
            case 'show':
                return 't' # TODO with caveats
            case _:
                return 'f'


    def call(self, **kwargs):
        options = {}
        allowed_keys = {'query', 'offset', 'limit', 'permissions'}
        options.update((k, v) for k, v in kwargs.items() if k in allowed_keys)
        clause, ids = self.visibility_clause(options.get('permissions'))
        can_see_private = self.can_see_private(options.get('permissions'))
        sql_query = "\n".join([self.header(), clause, self.footer()])
        print(sql_query)

        data = {
            'query': options.get('query'),
            'limit': options.get('limit', 20),
            'offset': options.get('offset', 0),
            'ids': ids,
            'can_see_private': can_see_private
        }

        with connection.cursor() as cursor:
            cursor.execute(sql_query, data)
            return self.dictfetchall(cursor)


    def header(self):
        return """
        WITH myconstants (can_see_private) as (
            values (%(can_see_private)s)
        )
        SELECT
        (   CASE public
            WHEN 't' THEN id
            WHEN 'f' THEN
              CASE can_see_private
              WHEN 't' THEN id
              WHEN 'f' THEN NULL
              END
            END
        ) as id,
        (   CASE public
            WHEN 't' THEN filename
            WHEN 'f' THEN
              CASE can_see_private
              WHEN 't' THEN filename
              WHEN 'f' THEN NULL
              END
            END
        ) as filename,
        title,
        public,
        ts_rank_cd(search_text, query) AS rank,
        (   CASE public
            WHEN 't' THEN preview
            WHEN 'f' THEN
              CASE can_see_private
              WHEN 't' THEN preview
              WHEN 'f' THEN NULL
              END
            END
        ) as highlight,
        (   CASE public
            WHEN 't' THEN 't'
            WHEN 'f' THEN can_see_private
            END
        ) as visible
        FROM
            search_document,
            websearch_to_tsquery(%(query)s) query,
            ts_headline(
                body,
                query,
                $$MaxFragments=0, MaxWords=40, MinWords=30, StartSel='<span class="highlight">', StopSel='</span>'$$
            ) preview,
            myconstants
        WHERE query @@ search_text
        """


    def footer(self):
        return """
        ORDER BY rank DESC
        LIMIT %(limit)s
        OFFSET %(offset)s;
        """
