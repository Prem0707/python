# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    # return render(request, 'blog/index.html', context={
    #     'title': '我的博客首页',
    #     'welcome': '欢迎访问我的博客首页'
    # })

    post_list = Post.objects.all().order_by('-created_time')
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()

    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={
        'post_list': posts,
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