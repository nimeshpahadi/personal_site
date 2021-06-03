from . import views
from django.urls import path, re_path, include
from .feeds import LatestPostsFeed

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/<slug:slug>/', views.post_detail, name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]