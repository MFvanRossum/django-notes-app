from django.db import models
from django.utils.text import slugify

class Note(models.Model):
    title = models.CharField(max_length=280)
    body = models.TextField(max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"Note Title: {self.title} Body: {self.body}"

class Tag(models.Model):
    name = models.CharField(max_length=40)
    slug = slugify(name)