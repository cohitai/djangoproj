from django.shortcuts import render
from .models import Article

# Create your views here.


def home(req):
    all_articles = Article.objects.all().order_by('-id')[0:1000]
    return render(req, 'home.html',{'all':all_articles})