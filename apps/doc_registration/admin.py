from django.utils.safestring import mark_safe
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.urls import reverse

from apps.doc_registration.models import (Area,
                                          Source,
                                          Category,
                                          Document,
                                          DocumentDetails,
                                          Mandate,
                                          MandateTest
                                          )


def get_edit_link(self, obj=None):
    if obj.pk:  # if object has already been saved and has a primary key, show link to it
        change_url = reverse('admin:%s_%s_change' % (
            obj._meta.app_label, obj._meta.model_name), args=[obj.pk]
        )
        delete_url = reverse('admin:%s_%s_delete' % (
            obj._meta.app_label, obj._meta.model_name), args=[obj.pk]
        )
        return mark_safe(f'''
                <a href="{change_url}">
                    <input type='button' style="float: none; background: #417690" class="default" value='Ir' />
                </a>
                <a href="{delete_url}">
                    <input type='button' style="float: none; background: #a41515" class="default" value='Eliminar' />
                </a>
            ''')
    return ''


class BaseInline(admin.TabularInline):
    get_edit_link = get_edit_link
    get_edit_link.short_description = "Acciones"
    readonly_fields = ('get_edit_link', )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def has_delete_permission(self, request, obj=None):
        return False


class MandateTestInline(BaseInline):

    model = MandateTest
    fields = ('name', 'description', 'get_edit_link')
    ordering = ('id',)


class MandateInline(BaseInline):

    model = Mandate
    fields = ('content', 'areas', 'category', 'get_edit_link')
    ordering = ('id',)
    readonly_fields = ('get_edit_link', )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 9, 'cols': 100})},
    }


class DocumentDetailsInline(BaseInline):

    model = DocumentDetails
    fields = ('file_name', 'document_date', 'link', 'get_edit_link')
    ordering = ('document_date',)
    readonly_fields = ('get_edit_link', )


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
    search_fields = ('content', 'document_ref__document__title')
    autocomplete_fields = ('category', 'document_ref')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 7, 'cols': 120})},
    }

    inlines = [
        MandateTestInline
    ]


class DocumentDetailsAdmin(admin.ModelAdmin):
    search_fields = ('document__title', )
    fields = ('link', 'document', 'file_name',
              'document_date',)
    autocomplete_fields = ('document', )

    inlines = [
        MandateInline
    ]


admin.site.register(Area, AreaAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Mandate, MandateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentDetails, DocumentDetailsAdmin)
admin.site.register(MandateTest)
