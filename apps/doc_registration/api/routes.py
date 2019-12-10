from rest_framework.response import Response
from rest_framework import routers, viewsets
from .serializers import *
from django.conf.urls import url, include
from apps.doc_registration.models import *


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def retrieve(self, request, pk):
        areas = Area.objects.filter(
            mandate__document_ref_id=pk
        ).distinct()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk):

        categories = Category.objects \
            .filter(mandate__document_ref_id=pk) \
            .distinct()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetailsViewSet(viewsets.ModelViewSet):
    queryset = DocumentDetails.objects.all()
    serializer_class = DocumentDetailsSerializer


class MandateTestViewSet(viewsets.ModelViewSet):
    queryset = MandateTest.objects.all()
    serializer_class = MandateTestSerializer


class InfoViewSet(viewsets.ViewSet):

    def list(self, request, pk=None):

        mandates = Mandate.objects.count()
        tests = MandateTest.objects.count()
        documents = Document.objects.count()
        sources = Source.objects.count()

        response = {
            'mandates': mandates,
            'tests': tests,
            'documents': documents,
            'sources': sources,
        }

        return Response(response)


class MandateViewSet(viewsets.ModelViewSet):
    queryset = Mandate.objects.all()
    serializer_class = MandateSerializer

    def get_queryset(self):
        area = self.request.query_params.get('area')
        category = self.request.query_params.get('category')
        text = self.request.query_params.get('text')
        doc_ref = self.request.query_params.get('document_detail')

        queryset = Mandate.objects.filter()

        if doc_ref: queryset = queryset.filter(document_ref=doc_ref)
        if area: queryset = queryset.filter(areas=area)
        if category: queryset = queryset.filter(category=category)
        if text: queryset = queryset.filter(content__icontains=text)

        return queryset
        

router = routers.DefaultRouter()

router.register('info', InfoViewSet, base_name='info')
router.register('area', AreaViewSet)
router.register('category', CategoryViewSet)
router.register('source', SourceViewSet)
router.register('mandate', MandateViewSet)
router.register('document', DocumentViewSet)
router.register('mandate_tests', MandateTestViewSet)
router.register('document_details', DocumentDetailsViewSet)
