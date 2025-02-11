from search.repositories.search_results import SearchResultsRepository
from search.operations.document_visibility_engine import DocumentVisibilityEngine
from search.repositories.users import UsersRepository

class DocumentSearch:

    default_searcher = UsersRepository.first()

    def __init__(
            self,
            query: str,
            searcher = None,
            engine = DocumentVisibilityEngine()
        ):
        self.query = query
        self.person = searcher or self.default_searcher
        self.engine = engine


    def call(self):
        permissions = self.engine.call(
            self.person.role,
            case_ids = list(map(lambda case : case.id, self.person.cases.all())),
            region_ids = [self.person.region_id]
        )
        return SearchResultsRepository().all(
            query = self.query,
            permissions = permissions
        )
