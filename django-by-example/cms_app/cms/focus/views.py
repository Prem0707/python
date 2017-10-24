from django.shortcuts import render
from .models import Article, Comment, Poll, NewUser
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def index(request):
    latest_article_list = Article.objects.query_by_time()
    loginform = LoginForm()
    context = {'latest_article_list': latest_article_list, 'loginform':loginform}
    return render(request, 'index.html', context)
#