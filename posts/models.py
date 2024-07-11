from uuid import uuid4
from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    post_author = models.CharField(max_length=50, null=False, blank=False)
    post_content = models.TextField()
    post_title = models.CharField(max_length=100)
    post_resume = models.TextField()
    post_likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    comment_post_id = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )
    comment_author = models.CharField(max_length=50, null=False, blank=False)
    comment_content = models.TextField()
    comment_likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.comment_author} on {self.comment_post_id.post_title}"
