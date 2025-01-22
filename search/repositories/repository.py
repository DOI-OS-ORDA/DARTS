class Repository:
    def call(self, **kwargs):
        return list(
            map(
                lambda record : self.struct(record),
                self.relation().call(**kwargs)
            )
        )
