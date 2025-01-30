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
        self.user = searcher or self.default_searcher
        self.engine = engine


    def call(self):
        permissions = self.engine.call(
            self.user.role,
            case_ids = list(map(lambda case : case.id, self.user.cases.all())),
            # WARNING: This will error if the user does not have an assigned region
            region_ids = [self.user.region.id]
        )
        return SearchResultsRepository().all(
            query = self.query,
            permissions = permissions
        )
