from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

# TEMPLATE TAGGING

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/search', views.SearchBlog.as_view(), name='blog-search'),
    path('post/tags/<slug:tag_slug>/',
         views.TagListView.as_view(), name='posts_by_tag'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/new', views.PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update',
         views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete',
         views.PostDeleteView.as_view(), name='post-delete'),
    path('about_us', views.about, name='blog-about'),
]
