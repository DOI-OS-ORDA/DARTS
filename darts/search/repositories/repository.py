import functools

from search.structs.struct import Struct


class Repository:
    struct = Struct

    def find_or_create(self, pk, data={}):
        try:
            return self.find(pk)
        except:  # noqa: E722
            return self.add({"id": pk} | data)

    def find(self, pk):
        match self.ancestor():
            case "model":
                return self.relation.objects.get(pk)
            case "repo":
                raise

    def get(self, pk):
        return self.find(pk)

    def first(self):
        match self.ancestor():
            case "model":
                return self.relation.objects.first()
            case "repo":
                raise

    def add(self, data):
        match self.ancestor():
            case "model":
                record = self.relation(**data)
                record.save()
                return record
            case "repo":
                return self.relation.add(data)

    def all(self, **kwargs):
        return list(
            map(lambda record: self.struct(record), self.relation().all(**kwargs))
        )

    def call(self, **kwargs):
        return list(
            map(lambda record: self.struct(record), self.relation().call(**kwargs))
        )

    @functools.cache
    def ancestor(self):
        if "ModelBase" in self.ancestors():
            return "model"
        elif "Repository" in self.ancestors():
            return "repo"
        else:
            raise

    def ancestors(self):
        return list(map(lambda x: x.__class__.__name__, self.relation.mro()))
