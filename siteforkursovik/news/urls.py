from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news'),
    path('NewsModeration', views.Moderation_News, name='ModerationNews'),
    path('MyNews', views.MyNews, name='MyNews'),
    path('create', views.NewsCreateView.as_view(), name='create'),
    path('<slug:slug>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<slug:slug>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<slug:slug>/update_moderator', views.NewsUpdateModeratorView.as_view(), name='news-update-moderator'),
    path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]