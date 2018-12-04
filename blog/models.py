from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.title

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def get_absolute_url(self):
      return reverse("blog:post_detail", kwargs={"post_id": self.pk})

class Comment(models.Model):
  post = models.ForeignKey('blog.Post', related_name='comments')
  nickname = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.text