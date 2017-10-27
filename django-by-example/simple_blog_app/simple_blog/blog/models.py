from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


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
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     # 'blog:detail': blog 应用下的 name=detail 的函数
    #     return reverse('blog:detail', kwargs={'pk': self.pk})
    #
    # def increase_views(self):
    #     self.views += 1
    #     self.save(update_fields=['views'])