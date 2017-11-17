from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime


def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'index.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})
