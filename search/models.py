from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
from django.template.defaultfilters import slugify

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
    # slug should be null=False, unique=True, default=slugify(self.title) but can't figure out how to do that.
    slug = models.SlugField(max_length=255, null=True)
    public = models.BooleanField(default=False)

    # belongs_to :case
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)

    # belongs_to :region, through: :case
    def region(self):
        if self.case:
            return self.case.region

    def save(self, *args, **kwargs):  # new
        if self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

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

    def get_absolute_url(self):
        return reverse("document", kwargs={ "id": str(self.id), "slug": str(self.slug) })


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)

    GUEST = "guest"
    SUPERUSER = "superuser"
    TECH = "tech"
    STAFF = "staff"
    REGIONAL = "regional"
    ROLES = {
        GUEST:     "Guest user",
        SUPERUSER: "Superuser",
        TECH:      "Tech support",
        STAFF:     "Staff",
        REGIONAL:  "Regional coordinator",
    }
    role = models.CharField(max_length=9, choices=ROLES)

    def role_name(self):
        return self.ROLES[self.role]

    # has_and_belongs_to_many :cases
    cases = models.ManyToManyField(Case, blank=True)

    # belongs_to :region
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
