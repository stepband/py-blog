from django.contrib.auth.views import LoginView
from django.urls import path

from .views import PostDetailView, IndexView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    path(
        '', IndexView.as_view(),
        name='index'
        ),
    path(
        'posts/<int:pk>/',
        PostDetailView.as_view(),
        name='post-detail'
        ),
    path(
        "posts/<int:pk>/comment/create/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
   ]

