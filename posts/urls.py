from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:id>', views.details, name='details'),
    path('posts/add_comment/<int:id>', views.add_comment, name="add_comment")
    ]
