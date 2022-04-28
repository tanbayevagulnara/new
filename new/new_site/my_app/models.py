from audioop import reverse
from importlib.resources import contents
from turtle import title
from django.db import models


# Create your models here.


class First(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "step"
        verbose_name_plural = "steps"
        ordering = ['title', '-content']


class Second(models.Model):
    title = models.CharField(max_length=255, verbose_name="Name")
    is_published = models.BooleanField(default=True, verbose_name="Is it published")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('music', kwargs={'title_slug': self.slug})

    class Meta:
        verbose_name = "music"
        verbose_name_plural = "all the music"
