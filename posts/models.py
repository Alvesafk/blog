from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return f"{self.id}, {self.name}"

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    preview = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name="tags")
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    publish_date = models.DateTimeField(blank=True, null=True)

    @property
    def tags_string(self):
        tag_list = [c.name for c in self.tags.all()]
        return ", ".join(tag_list) if tag_list else ""

    @property
    def auto_preview(self):
        return self.content[:256] + "."

    def __str__(self):
        return f"{self.title}, {self.tags}, {self.publish_date}"
