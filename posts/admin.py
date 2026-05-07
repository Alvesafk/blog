from django.contrib import admin
from .models import Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "tags_string", "publish_date")

class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class CommentAdmin(admin.ModelAdmin):
    list_display= ("id", "post_related_to", "author", "publish_date")

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
