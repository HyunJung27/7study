from django.db import models
from django import forms

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    board = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.board.pk, self.pk])
