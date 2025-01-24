from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Region(models.Model):
    name = models.TextField()
    number = models.IntegerField()
    # has_many :cases

    def __str__(self):
        return f"Region {self.number}: {self.name}"


class Case(models.Model):
    name = models.TextField()
    public = models.BooleanField(default=False)
    # has_many :documents
    # belongs_to :region
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    body = models.TextField()
    file = models.BinaryField()
    filename = models.CharField(max_length=255)
    filename_normal = models.CharField(max_length=255)
    search_text = SearchVectorField()
    title = models.CharField(max_length=255)
    public = models.BooleanField(default=False)

    # belongs_to :case
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)

    # belongs_to :region, through: :case
    def region(self):
        if self.case:
            return self.case.region

    # Override insert and update methods to prevent inserting/updating search_text directly
    def _do_insert(self, manager, using, fields, update_pk, raw):
        return super(Document, self)._do_insert(
            manager, using,
            [f for f in fields if f.attname not in ['search_text']],
            update_pk, raw)

    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        return super(Document, self)._do_update(
            base_qs, using, pk_val,
            [f for f in values if f[0].attname not in ['search_text']],
            update_fields, forced_update)

    def __str__(self):
        return self.title
