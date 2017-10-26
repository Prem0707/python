# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag

def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    # return render(request, 'blog/index.html', context={
    #     'title': '我的博客首页',
    #     'welcome': '欢迎访问我的博客首页'
    # })

    post_list = Post.objects.all().order_by('-created_time')
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
        'category_list': category_list,
        'tag_list': tag_list,
        'title': '博客列表',

    })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    return render(request, 'blog/detail.html', context={
        'post': post,
        'category_list': category_list,
        'tag_list': tag_list,
    })