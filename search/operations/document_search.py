from search.repositories.search_results import SearchResultsRepository

class DocumentSearch:

    def __init__(self, query: str):
        self.query = query

    def call(self):
        return SearchResultsRepository().call(self.query)
