from search.models import Person
from search.repositories.repository import Repository
from search.structs.struct import Struct

class UsersRepository(Repository):

    @classmethod
    def get(self, id):
        return Person.objects.get(pk=id)


    @classmethod
    def first(self):
        return Person.objects.first()


    @classmethod
    def all(self):
        return Person.objects.all()


    @classmethod
    def get_or_fallback(self, id):
        try:
            return self.get(id)
        except Person.DoesNotExist:
            return self.fallback()


    @classmethod
    def fallback(self):
        return Struct({
            'full_name': "Guest user",
            'role':      "guest",
            'role_name': "guest",
            'cases': Struct({ 'all': (lambda: []) }),
            'region': Struct({ 'id': None }),
        })
