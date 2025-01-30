from search.models import Person
from search.repositories.repository import Repository

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
