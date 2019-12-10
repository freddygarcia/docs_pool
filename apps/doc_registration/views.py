from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse

from json import dumps

from app import settings
from apps.doc_registration.models import Mandate
from apps.noticrawler.models import Post


def index(request):
    return redirect('/home')


def home(request):
    return render(request, 'list.html')
