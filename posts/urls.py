from django.urls import path
from posts.views import list_posts

urlpatterns = [
    path("", list_posts, name="posts_list"),
]