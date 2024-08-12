from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Create your models here.


class Blog(models.Model):
    # author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    content = RichTextField()
    time = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category", related_name="blog", on_delete=models.CASCADE, default=None
    )
    tags = models.ManyToManyField("Tags", related_name="blogs", default=None)

    def __str__(self):
        return self.author


class Category(models.Model):
    title = models.CharField(
        max_length=50,
    )
    slug = models.SlugField()
    time_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    time_published = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey("Blog", related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
