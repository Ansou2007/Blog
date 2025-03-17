from django.urls import path

from app.views import  ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView

urlpatterns = [
    #path('', views.index, name='index'),


    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]