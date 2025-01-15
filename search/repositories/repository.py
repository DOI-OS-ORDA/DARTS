class Repository:
    def call(self, *args):
        return list(
            map(
                lambda record : self.struct(record),
                self.relation().call(*args)
            )
        )
