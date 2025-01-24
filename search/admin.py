from django.contrib import admin

from search.models import Case, Document, Region

# Register your models here.

class CaseAdmin(admin.ModelAdmin):
    list_display = ["name", "region__name", "public"]
    ordering = ('pk',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ["title", "filename", "case__id", "public", "region",]
    ordering = ('-pk',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "number"]
    ordering = ('number',)

admin.site.register(Case, CaseAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Region, RegionAdmin)
