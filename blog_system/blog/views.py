from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post, User, Commentary


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail_view.html'
    context_object_name = 'post'

