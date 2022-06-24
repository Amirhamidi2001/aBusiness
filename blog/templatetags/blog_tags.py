from os import stat
from unicodedata import category
from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-recent-post.html')
def post_recent():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-category.html')
def post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories' : cat_dict}
