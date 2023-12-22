from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news'),
    path('NewsModeration', views.Moderation_News, name='ModerationNews'),
    path('MyNews', views.MyNews, name='MyNews'),
    path('create', views.NewsCreateView.as_view(), name='create'),
    path('<slug:slug>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/update_moderator', views.NewsUpdateModeratorView.as_view(), name='news-update-moderator'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]