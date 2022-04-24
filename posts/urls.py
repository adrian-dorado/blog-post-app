from django.urls import path
from posts.views import list_posts, create_post, posts_detail

urlpatterns = [
    path("", list_posts, name="posts_list"),
    path("new/", create_post, name="create_post"),
    path("<int:id>/", posts_detail, name="posts_detail"),
]