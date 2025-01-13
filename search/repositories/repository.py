class Repository:
    def call(self, *args):
        return list(
            map(
                lambda result : self.struct(result),
                self.relation().call(*args)
            )
        )
