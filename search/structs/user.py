from search.structs.struct import Struct

class UserStruct(Struct):
    def __init__(self, input: dict):
        super().__init__(input)

    def case_ids(self):
        return [1,2,3]

    def region_ids(self):
        return [3,4,5]
