from search.relations.relation import Relation
from django.db import connection

class SearchResultsRelation(Relation):


    # (%s, %s, %s) case_ids.times.map { "%s" }.join(",")

    def call(self, **kwargs):
        options = {}
        allowed_keys = {'query', 'offset', 'limit', 'permissions'}
        options.update((k, v) for k, v in kwargs.items() if k in allowed_keys)
        sql_query = "\n".join([
            self.returnable(options),
            self.visible(options)
        ])
        print("---->")
        print(options)
        print(sql_query)

        data = {
            'query': options.get('query'),
            'limit': options.get('limit', 20),
            'offset': options.get('offset', 0),
            # 'case_ids': options.get('permissions').get('case_ids', []),
            # 'region_ids': options.get('permissions').get('region_ids', []),
        }

        with connection.cursor() as cursor:
            cursor.execute(sql_query, data)
            results = self.dictfetchall(cursor)
            print(results)
            return results


    def returnable(self, options):
        return """
            WITH base as (
                SELECT
                    id,
                    filename,
                    title,
                    public,
                    ts_rank_cd(search_text, query) AS rank,
                    preview,
                    CAST(trunc((id / 3) + 1) AS INTEGER) as case_id,
                    CAST(trunc((id / 4) + 1) AS INTEGER) as region_id
                FROM
                    search_document,
                    websearch_to_tsquery(%(query)s) query,
                    ts_headline(
                      body,
                      query,
                      $$MaxFragments=0, MaxWords=40, MinWords=30, StartSel='<span class="highlight">', StopSel='</span>'$$
                    ) preview
                WHERE query @@ search_text
                ORDER BY rank DESC
                LIMIT %(limit)s
                OFFSET %(offset)s
            )
        """

    def visibility_clause(self, options):
        match options['permissions']:
            case 'hide':
                return "WHERE public = 't'"
            case {'case_ids': case_ids}:
                ids = tuple(case_ids)
                replaceable = ",".join(["%d"] * len(ids))
                return f"WHERE public = 't' OR (public = 'f' AND case_id IN ({replaceable}))" % ids
            case {'region_ids': region_ids}:
                ids = tuple(region_ids)
                replaceable = ",".join(["%d"] * len(ids))
                return f"WHERE public = 't' OR (public = 'f' AND region_id IN ({replaceable}))" % ids
            case 'show':
                return "WHERE public = 't' OR public = 'f'"
            case _:
                return "WHERE public = 't'"


    def visibility_clause_2(self, options):
        base = """
            UNION ALL
            SELECT
              NULL as id,
              case_id,
              region_id,
              public,
              FALSE as visible,
              title,
              NULL as preview,
              rank
            from base
        """
        match options['permissions']:
            case {'case_ids': case_ids}:
                ids = tuple(case_ids)
                replaceable = ",".join(["%d"] * len(ids))
                return base + f"WHERE (public = 'f' AND case_id NOT IN ({replaceable}))" % ids
            case {'region_ids': region_ids}:
                ids = tuple(region_ids)
                replaceable = ",".join(["%d"] * len(ids))
                return base + f"WHERE (public = 'f' AND region_id NOT IN ({replaceable}))" % ids
            case _:
                return ""

    def visible(self, options):
        return """
            (
                SELECT
                  id,
                  case_id,
                  region_id,
                  public,
                  TRUE as visible,
                  title,
                  preview,
                  rank
                from base
        """ + self.visibility_clause(options) + self.visibility_clause_2(options) + ") ORDER BY rank DESC"
