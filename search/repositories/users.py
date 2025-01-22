from search.repositories.repository import Repository
from search.structs.struct import Struct

class UsersRepository(Repository):

    @classmethod
    def get(self, slug):
        return next(user for user in self.all() if user.slug == slug)


    @classmethod
    def all(self):
        return [
            Struct({ 'name': "Guest user",          'slug': "guest" }),
            Struct({ 'name': "Staff",               'slug': "staff" }),
            Struct({ 'name': "Superuser",           'slug': "superuser" }),
            Struct({ 'name': "Tech support",        'slug': "tech-support" }),
            Struct({ 'name': "Regional coordinator", 'slug': "regional-coordinator" }),
        ]

    def call(self):
        pass
