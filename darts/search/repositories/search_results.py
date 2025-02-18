from search.repositories.repository import Repository
from search.relations.search_results import SearchResultsRelation
from search.structs.search_result import SearchResultStruct

class SearchResultsRepository(Repository):
    relation = SearchResultsRelation
    struct = SearchResultStruct
