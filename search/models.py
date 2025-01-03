from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Document(models.Model):
    filename = models.CharField(max_length=255)
    file = models.BinaryField()
    body = models.TextField()
    search_text = SearchVectorField()

    # Override the method to prevent it from inserting search_text
    def _do_insert(self, manager, using, fields, update_pk, raw):
        return super(Document, self)._do_insert(
            manager, using,
            [f for f in fields if f.attname not in ['search_text']],
            update_pk, raw)

    def __str__(self):
        return f"filename: {self.filename}, body: {self.body[:20]}"
