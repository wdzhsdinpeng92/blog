from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect

from backweb.Artform import AddArtForm, EditArtForm, AddCateForm, UpdateCateForm
from backweb.models import MyUser, Article, Column


def index(request):
    if request.method == 'GET':
        return render(request,'backweb/index.html')
    if request.method == 'POST':
        truename = request.POST.get('truename')
        username = request.POST.get('username')
        usertel = request.POST.get('usertel')
        old_password = request.POST.get('old_password')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        user = MyUser.objects.filter(username=username).first()
        if not user:
            err_name = '用户名不存在'
            return render(request, 'backweb/index.html', {'err_name': err_name})
        if old_password != user.password:
            err_name = '密码错误'
            return render(request, 'backweb/index.html', {'err_name': err_name})
        if password != new_password:
            err_name = '两次输入的密码不同'
            return render(request, 'backweb/index.html', {'err_name': err_name})
        MyUser.objects.filter(username=username).update(truename=truename,usertel=usertel,password=password)
        return render(request, 'backweb/index.html')




def login(request):
    if request.method == 'GET':
        return  render(request,'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = MyUser.objects.filter(username=username).first()
        if not user:
            err_name = '用户名不存在'
            return render(request, 'backweb/login.html', {'err_name': err_name})
        if password != user.password:
            err_name = '密码错误'
            return render(request, 'backweb/login.html', {'err_name': err_name})
        request.session['user_id'] = user.id
        res = HttpResponseRedirect('/backweb/index/')
        return res


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/backweb/index/')



def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        articles = Article.objects.all()
        paginator = Paginator(articles,7)
        page = paginator.page(page)
        return render(request,'backweb/article.html',{'page':page})

def add_article(request):
    if request.method == 'GET':
        categorys = Column.objects.all()
        return render(request,'backweb/add-article.html',{'categorys':categorys})
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags']
            visibility = form.cleaned_data['visibility']
            keywords = form.cleaned_data['keywords']
            titlepic = form.cleaned_data['titlepic']
            Article.objects.create(title=title, describe=describe, content=content, column_id=category,visibility=visibility,keywords=keywords,titlepic=titlepic,tags=tags)
            # return HttpResponseRedirect('/article/art/')
            return HttpResponseRedirect('/backweb/article/')

        else:
            return render(request, 'backweb/add-article.html', {'form': form})


def del_article(request,id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect('/backweb/article/')


def edit_article(request,id):
    if request.method == 'GET':
        categorys = Column.objects.all()
        article = Article.objects.filter(pk=id).first()
        return render(request,'backweb/add-article.html',{'article':article,'categorys':categorys})
    if request.method == 'POST':
        form = EditArtForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags']
            visibility = form.cleaned_data['visibility']
            keywords = form.cleaned_data['keywords']
            titlepic = form.cleaned_data['titlepic']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.describe = describe
            article.content = content
            article.category = category
            article.tags = tags
            article.visibility = visibility
            article.keywords = keywords
            if titlepic:
                article.titlepic = titlepic
            article.save()
            return HttpResponseRedirect('/backweb/article/')
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request,'backweb/add-article.html',{'form': form,'article':article})


def category(request):
    if request.method == 'GET':
        categorys = Column.objects.all()
        for i in categorys:
            i.count = i.article_set.count()
        return render(request,'backweb/category.html',{'categorys':categorys})
    if request.method == 'POST':
        form = AddCateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            keywords = form.cleaned_data['keywords']
            describe = form.cleaned_data['describe']
            father_id = request.POST.get('fid')
            if father_id:
                Column.objects.create(name=name,alias=alias,keywords=keywords,describe=describe,father_id=father_id)
            else:
                Column.objects.create(name=name,alias=alias,keywords=keywords,describe=describe)
            return HttpResponseRedirect('/backweb/category/')

        else:
            return render(request, 'backweb/category.html', {'form': form})

def del_category(request,id):
    if request.method == 'GET':
        Article.objects.filter(column_id=id).delete()
        Column.objects.filter(pk=id).delete()
        return HttpResponseRedirect('/backweb/category/')


def update_category(request,id):
    if request.method == 'GET':
        category = Column.objects.filter(pk=id).first()
        categorys = Column.objects.all()
        return render(request, 'backweb/update-category.html', {'category': category,'categorys': categorys})
    if request.method == 'POST':
        form = UpdateCateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            keywords = form.cleaned_data['keywords']
            describe = form.cleaned_data['describe']
            father_id = request.POST.get('fid')
            category = Column.objects.filter(pk=id).first()
            category.name = name
            category.alias = alias
            category.keywords = keywords
            category.describe = describe
            category.father_id = father_id
            category.save()
            return HttpResponseRedirect('/backweb/category/')
        else:
            return render(request, 'backweb/category.html', {'form': form})

