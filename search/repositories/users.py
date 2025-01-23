from search.repositories.repository import Repository
from search.structs.user import UserStruct

class UsersRepository(Repository):

    @classmethod
    def get(self, slug):
        return next(user for user in self.all() if user.slug == slug)


    @classmethod
    def all(self):
        return [
            UserStruct({ 'name': "Guest user",   'slug': "guest" }),
            UserStruct({ 'name': "Superuser",    'slug': "superuser" }),
            UserStruct({ 'name': "Tech support", 'slug': "tech-support" }),
            UserStruct({ 'name': "Staff",               'slug': "staff" }),
            UserStruct({ 'name': "Regional coordinator", 'slug': "regional-coordinator" }),
        ]


    def call(self):
        pass
