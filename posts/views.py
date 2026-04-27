from django.shortcuts import render
from .models import Post

def index(request):
    all_posts = Post.objects.all()

    context = {
            "all_posts": all_posts,   
    }

    return render(request, 'index.html', context)
