from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Document(models.Model):
    filename = models.CharField(max_length=255)
    file = models.BinaryField()
    body = models.TextField()
    search_text = SearchVectorField()

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        book.save()
        return book
