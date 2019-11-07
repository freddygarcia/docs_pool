from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from json import dumps

from app import settings
from .forms import SearchForm
from apps.doc_registration.models import Mandate
from apps.noticrawler.models import Post


def index(request):
     return redirect('/home')

def home(request):
    this_week_posts, older_posts = Post.recent_posts()
    context = { 'f_filters' : {}, 'this_week_posts' : this_week_posts, 'older_posts' : older_posts}

    if request.method == 'POST':
        filters = request.POST
        mandates_list = Mandate.find(filters)
        paginator = Paginator(mandates_list, settings.PAGE_LIMIT)

        page = filters.get('page', 1)
        mandates = paginator.get_page(page)

        json = filters.dict()
        context = { 'mandates' : mandates, 'f_filters' : json, 'this_week_posts' : this_week_posts, 'older_posts' : older_posts}
        return render(request, 'list.html', context)

    return render(request, 'list.html', context)


def mandate(request, mandate_id):
    mandate = Mandate.objects.get(pk=mandate_id)
    context = {'mandate': mandate}
    return render(request, 'single.html', context)