from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey('auth.User')
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