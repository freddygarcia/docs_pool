from django_select2.forms import  ModelSelect2Widget

from django import forms
from apps.doc_registration.models import Area, Source, Category, Document, DocumentDetails, Mandate


class SearchForm(forms.Form):

    area = forms.IntegerField(required=False)
    source = forms.IntegerField(required=False)
    category = forms.IntegerField(required=False)
