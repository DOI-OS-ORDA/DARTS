from django.db import models
from django.contrib.postgres.search import SearchVectorField

# Officially, storing files in db "is bad design in 99% of the cases"
# https://docs.djangoproject.com/en/5.1/ref/models/fields/#binaryfield
class Document(models.Model):
    file_name = models.CharField(max_length=255)
    file_binary = models.BinaryField()
    file_text = models.TextField()
    search_text = SearchVectorField()

