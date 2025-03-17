from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import Article
from django.urls import reverse_lazy

# Create your views here.



# Liste Article
class ArticleListView(ListView):
    model = Article
    template_name = "post.html"
    context_object_name = "articles"
    paginate_by = 4

class ArticleDetailView(DetailView):
    model = Article
    template_name = "details.html"

class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = "blog/article_form.html"
    success_url = reverse_lazy('article_list')

# Modification Article
class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = "modifier.html"
    success_url = reverse_lazy('article_list')


# Suppression Article
class ArticleDeleteView(DeleteView):
    model = Article
    fields = ['titre']
    template_name = "supprimer.html"
    success_url = reverse_lazy('article_list')