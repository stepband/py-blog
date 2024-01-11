from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post, User, Commentary


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 2
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

