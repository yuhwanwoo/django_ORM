from django.shortcuts import render, redirect
import requests
#모델 가져오기
from articles.models import Article

# Create your views here.

# 전체 데이터 가져오기
# 그 데이터 템플릿에게 넘겨주기
# 템플릿에서 반복문으로 각각의 게시글 pk, title 보여주기
def index(request):
    article=Article.objects.all()
    context={
        'articles':article
    }
    return render(request,'articles/index.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title=request.POST.get('title')
    text=request.POST.get('text')
    Article.objects.create(title=title,content=text)
    return redirect('articles:index')


# 1. /introduce/
# 2. h1 태그로 이루어진 제목
# 2-1. 각각의 p 태그에 이름과 나이 작성
# 3. back링크로 index로 돌아갈 수 있는 링크 하나
# 4. index에서 introduce 이동할 수 있는 링크 하나
# 5. base.html 상속받아서 block body 안에 작성
def introduce(request):
    return render(request,'articles/introduce.html')

def detail(request,article_pk):
    #request.method
    article=Article.objects.get(pk=article_pk)
    if request.method=="POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail',article.pk)

def delete(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def edit(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    context={
        'article':article
    }
    return render(request,'articles/edit.html',context)

def update(request,article_pk):
    edit_title=request.POST.get('edit_title')
    edit_content=request.POST.get('edit_content')
    article=Article.objects.get(pk=article_pk)
    article.title=edit_title
    article.content=edit_content
    article.save()
    return redirect('articles:detail',article_pk)