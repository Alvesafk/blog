from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return f"{self.id}, {self.name}"

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.tags}, {self.publish_date}"
