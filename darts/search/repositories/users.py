from search.models import Person
from search.repositories.repository import Repository
from search.structs.struct import Struct


class UsersRepository(Repository):
    relation = Person

    def get_or_fallback(self, pk):
        try:
            return self.get(pk)
        except (Person.DoesNotExist, TypeError):
            return self.fallback()

    def fallback(self):
        return Struct(
            {
                "full_name": "Guest user",
                "role": "guest",
                "role_name": "guest",
                "cases": Struct({"all": (lambda: [])}),
                "region": Struct({"id": None}),
                "region_id": None,
            }
        )
