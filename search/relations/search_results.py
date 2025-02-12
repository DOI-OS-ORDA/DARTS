from search.relations.relation import Relation
from django.db import connection

class SearchResultsRelation(Relation):

    def all(self, **kwargs):
        options = {}
        allowed_keys = {'query', 'offset', 'limit', 'permissions'}
        options.update((k, v) for k, v in kwargs.items() if k in allowed_keys)
        sql_query = "\n".join([
            self.returnable(options),
            self.visible(options),
            self.unpreviewable(options),
            self.sort(options)
        ])
        print("---->")
        print(options['permissions'])
        print(sql_query)

        data = {
            'query': options.get('query'),
            'limit': options.get('limit', 20),
            'offset': options.get('offset', 0),
        }

        with connection.cursor() as cursor:
            cursor.execute(sql_query, data)
            return self.dictfetchall(cursor)


    def returnable(self, options):
        return """
            WITH base as (
                SELECT
                    search_document.id,
                    search_document.filename,
                    search_document.slug,
                    search_document.title,
                    search_document.public,
                    ts_rank_cd(search_text, query) AS rank,
                    preview,
                    search_document.case_id,
                    search_region.id as region_id
                FROM
                    search_document
                        JOIN search_case ON case_id = search_case.id
                        JOIN search_region ON search_case.region_id = search_region.id,
                    websearch_to_tsquery('english', %(query)s) query,
                    ts_headline(
                      body,
                      query,
                      $$MaxFragments=0, MaxWords=40, MinWords=30, StartSel='<span class="highlight">', StopSel='</span>'$$
                    ) preview
                WHERE
                    query @@ search_text
                ORDER BY rank DESC
                LIMIT %(limit)s
                OFFSET %(offset)s
            )
        """

    def visible(self, options):
        return """
            (
                SELECT
                  id,
                  filename,
                  slug,
                  case_id,
                  region_id,
                  public,
                  TRUE as visible,
                  title,
                  preview,
                  rank
                from base
        """ + self.visibility_clause(options)


    def query_value(self, input_ids):
        return tuple(input_ids) or 'NULL'


    def query_placeholder(self, value):
        match value:
            case 'NULL':
                return '%s'
            case (xs):
                return ",".join(["%d"] * len(xs))


    def query_components(self, input_ids):
        value = self.query_value(input_ids)
        placeholder = self.query_placeholder(value)
        return placeholder, value


    def visibility_clause(self, options):
        match options['permissions']:
            case 'hide':
                return "WHERE public"
            case {'case_ids': case_ids}:
                placeholder, value = self.query_components(case_ids)
                return f"WHERE public OR (NOT public AND case_id IN ({placeholder}))" % value
            case {'region_ids': region_ids}:
                placeholder, value = self.query_components(region_ids)
                return f"WHERE public OR (NOT public AND region_id IN ({placeholder}))" % value
            case 'show':
                return "WHERE public OR NOT public"
            case _:
                return "WHERE public"


    def unpreviewable(self, options):
        base = """
            UNION ALL
            SELECT
              NULL as id,
              NULL as filename,
              NULL as slug,
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
                placeholder, value = self.query_components(case_ids)
                return base + f"WHERE (NOT public AND case_id NOT IN ({placeholder}))" % value
                #                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                #                                 Remove this if there are no cases assigned
            case {'region_ids': region_ids}:
                placeholder, value = self.query_components(region_ids)
                return base + f"WHERE (NOT public AND region_id NOT IN ({placeholder}))" % value
                #                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                #                                 Remove this if there are no regions assigned
            case _:
                return ""


    def sort(self, options):
        return ") ORDER BY rank DESC"
