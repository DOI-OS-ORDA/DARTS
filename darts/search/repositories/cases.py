from search.repositories.repository import Repository
from search.models import Case

class CasesRepository(Repository):
    relation = Case
