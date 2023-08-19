from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class PostStatus(models.IntegerChoices):
    DRAFT = 0, _("DRAFT")
    PUBLISHED = 1, _("PUBLISHED")


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=PostStatus.choices, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
