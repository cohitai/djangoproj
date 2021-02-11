from django.shortcuts import render
from .models import Article
from .models import BerlinerZeitung

# Create your views here.


def home(req):
    #all_articles = Article.objects.all().order_by('-id')[0:1000]
    all_articles_blz = BerlinerZeitung.objects.all().order_by('-id')[0:10]
    return render(req, 'home.html',{'all':all_articles_blz})