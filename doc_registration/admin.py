from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from doc_registration.models import Area, Source, Category, Document, DocumentDetails, Mandate


class DocumentDetailsInline(admin.TabularInline):

    model = DocumentDetails
    readonly_fields=('last_update',)
    fields = ('file_name', 'last_update', 'link')
    ordering = ('last_update',)

class DocumentAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'source__name')
    autocomplete_fields = ('source', )

    inlines = [
        DocumentDetailsInline
    ]

class SourceAdmin(admin.ModelAdmin):
    search_fields = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', )

class AreaAdmin(admin.ModelAdmin):
    search_fields = ('name', )

class MandateAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'source__name')
    autocomplete_fields = ('category', 'document')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':25, 'cols':170})},
    }


admin.site.register(Area, AreaAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Mandate, MandateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
