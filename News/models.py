from django.db import models
from django.conf import settings


class TimeStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Django won't make table after we have written this

class Category(TimeStamp):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Tag(TimeStamp):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Post(TimeStamp):
    STATUS_CHOICES = [
        ('active', 'Active'),  # First one for backend, second one for frontend
        ('in_active', 'Inactive'),
    ]
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d")
    published_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Active')
    # BigIntegerField means either positive or 0
    views_count = models.PositiveBigIntegerField(default=0)
    # category has 1 to Many Relationship with Post and Relation is always maintained in Many side for
    # 1 to Many Relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Since tag has many to many relationship so it doesn't matter where you place it
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    