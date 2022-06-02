from django.db import models

# Create your models here.
class Video(models.Model):
  title = models.CharField(max_length=255)
  category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
  youtube_link = models.URLField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title


class Category(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.name