from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post
# Create your views here.


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    post.counted_views = post.counted_views+1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if request.GET.get('s'):
            s = request.GET.get('s')
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
