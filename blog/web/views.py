from django.shortcuts import render

from backweb.models import Column, Article


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        categorys = Column.objects.all()
        for i in categorys:
            i.count = i.article_set.count()
        return render(request,'web/index.html',{'categorys':categorys,'articles':articles})
