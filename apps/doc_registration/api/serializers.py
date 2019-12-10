from rest_framework import serializers

from apps.doc_registration.models import *


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name']


class DocumentDetailsSerializer(serializers.ModelSerializer):

    mandates = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = DocumentDetails
        fields = ['id', 'link', 'file_name',
                  'document_date', 'document', 'mandates']


class DocumentSerializer(serializers.ModelSerializer):

    recent_details = serializers.IntegerField(source='recent_details.id')

    class Meta:
        model = Document
        fields = ['id', 'title', 'description', 'recent_details']


class MandateTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = MandateTest
        fields = '__all__'


class MandateSerializer(serializers.ModelSerializer):

    tests = MandateTestSerializer(
        many=True
    )

    class Meta:
        model = Mandate
        fields = ('display_content', 'tests')
