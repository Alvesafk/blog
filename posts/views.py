from django.shortcuts import get_object_or_404, render
from .models import Post

def index(request):
    return render(request, 'index.html')

def posts(request):
    all_posts = Post.objects.order_by("-publish_date").all()

    context = {
            "all_posts": all_posts,   
    }

    return render(request, 'posts.html', context)

def details(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
            "post": post,
    }

    return render(request, 'details.html', context)
