from django.contrib import admin

from search.models import Case, Document, Person, Region

# Register your models here.

class CaseAdmin(admin.ModelAdmin):
    list_display = ["name", "region", "public"]
    ordering = ('pk',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ["title", "public", "case", "region", "filename"]
    ordering = ('-pk',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ["full_name", "role", "region",]
    ordering = ('pk',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "number"]
    ordering = ('number',)

admin.site.register(Case, CaseAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Region, RegionAdmin)
