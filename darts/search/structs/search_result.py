from search.structs.struct import Struct

class SearchResultStruct(Struct):
    def __init__(self, input: dict):
        super().__init__(input)
        self.get_absolute_url = f"/documents/{self.id}/{self.slug}/"
