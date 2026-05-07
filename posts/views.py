from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .functions.random_username import get_random_username

def index(request):
    most_recent_post = Post.objects.order_by("-publish_date").first()

    context = {
        "most_recent_post": most_recent_post,
    }

    return render(request, 'index.html', context)

def posts(request):
    all_posts = Post.objects.order_by("-publish_date").all()

    context = {
            "all_posts": all_posts,   
    }

    return render(request, 'posts.html', context)

def details(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post_related_to=id).order_by('-publish_date').all()

    context = {
            "post": post,
            "comments": comments,
    }

    return render(request, 'details.html', context)

def add_comment(request, id):
    response = redirect('details', id)

    if not request.method == "POST":
        return response

    r_username = request.POST.get("username").strip()
    r_comment_content = request.POST.get("comment-input").strip()

    if not r_username:
        r_username = get_random_username()
        response.set_cookie(
                'username',
                r_username, 
                max_age=60*60*24*365,
                secure=True
                )

    c = Comment(
        content=r_comment_content,
        author=r_username,
        post_related_to=get_object_or_404(Post, id=id)
    )
    c.save()

    return response
