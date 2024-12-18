from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Document(models.Model):
    file_name = models.CharField(max_length=255)
    file_binary = models.BinaryField()
    file_text = models.TextField()
    search_text = SearchVectorField()

