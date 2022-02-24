from django import template
from blog.models import Post


register = template.Library()


@register.inclusion_tag('blog/recent_posts.html')
def load_recent_posts():
    recent_posts = Post.objects.all().order_by('-date_posted')[:5]
    return {'recent_posts': recent_posts}
