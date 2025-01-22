from search.repositories.search_results import SearchResultsRepository
from search.operations.document_visibility_engine import DocumentVisibilityEngine
from search.structs.struct import Struct

class DocumentSearch:

    default_searcher = Struct({ 'role': "", 'case_ids': [], 'region_ids': [] })

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
            case_ids = self.user.case_ids,
            region_ids = self.user.region_ids
        )
        return SearchResultsRepository().call(
            query = self.query,
            permissions = permissions
        )
