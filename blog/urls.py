from . import views
from django.urls import path
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>,<int:id>/', views.post_detail, name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]