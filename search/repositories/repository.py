class Repository:


    def all(self, **kwargs):
        return list(
            map(
                lambda record : self.struct(record),
                self.relation().all(**kwargs)
            )
        )

    def call(self, **kwargs):
        return list(
            map(
                lambda record : self.struct(record),
                self.relation().call(**kwargs)
            )
        )
