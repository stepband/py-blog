from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 5
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'