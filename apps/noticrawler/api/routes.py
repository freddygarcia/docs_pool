from rest_framework.response import Response
from rest_framework import routers, viewsets
from .serializers import *
from django.conf.urls import url, include
from apps.noticrawler.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


router = routers.DefaultRouter()

router.register('post', PostViewSet)
