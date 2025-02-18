class Relation:

    def dictfetchall(self, cursor):
        """
        Return all rows from a cursor as a dict.
        Assume the column names are unique.
        """
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def fetch_arg(self, index, default):
        try:
            return self.args[index]
        except IndexError:
            default
