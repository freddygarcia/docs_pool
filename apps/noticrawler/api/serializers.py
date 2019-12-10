from rest_framework import serializers

from apps.noticrawler.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['source_link', 'creation_date',
                  'title', 'body', 'image', 'url', 'is_sent']
