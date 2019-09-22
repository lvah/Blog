from django.shortcuts import render, get_object_or_404
import  markdown

# Create your views here.
from django.http import HttpResponse
from .models import Post, Category


def index(request):
    # 对于博客按照创建时间进行排序展示
    posts = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'posts': posts
    })


def detail(request, pk):
    # pk = id
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',

                                  ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    print(year, month)
    posts = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')

    return render(request, 'blog/index.html', context={'posts': posts})


def category(request, pk):
   # 记得在开始部分导入 Category 类
   cate = get_object_or_404(Category, pk=pk)
   posts = Post.objects.filter(category=cate).order_by('-created_time')
   return render(request, 'blog/index.html', context={'posts': posts})