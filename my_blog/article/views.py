from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
# Create your views here.


def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})
