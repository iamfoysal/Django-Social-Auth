from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=50)
    slag = models.SlugField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slag])

    def save(self, *args, **kwargs):
        self.slag = slugify(self.title)
        super().save(*args, **kwargs)