from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('分类', max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('标签', max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('文章标题', max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    excerpt = models.CharField('文章摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)