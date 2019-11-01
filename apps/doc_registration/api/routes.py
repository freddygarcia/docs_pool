from django.conf.urls import url, include
from apps.doc_registration.models import Area, Source, Category, Document
from rest_framework import routers, viewsets
from .serializers import *

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

router = routers.DefaultRouter()
router.register('area', AreaViewSet)
router.register('category', CategoryViewSet)
router.register('source', SourceViewSet)
router.register('document', DocumentViewSet)
