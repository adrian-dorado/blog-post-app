from django.shortcuts import render
from posts.models import Post

# Create your views here.
def list_posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "posts/main.html", context)