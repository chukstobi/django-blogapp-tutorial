from django import template
from blog.models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


register = template.Library()


@register.inclusion_tag('blog/recent_posts.html')
def load_recent_posts():
    recent_posts = Post.objects.all().order_by('-date_posted')[:5]
    return {'recent_posts': recent_posts}


@register.inclusion_tag('users/user_detail.html')
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return {"user": user}
