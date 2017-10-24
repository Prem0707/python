from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # 文章标题 CharField是字符字段，将会转化成SQL数据库varchar列
    title = models.CharField(max_length=250)
    # slug属性经常被用于URLs，slug只包含字母。数字、还有下划线。添加了unique_for_date参数，这表示每一个由模型创造的文章实例都有唯一的slug属性
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() #默认管理器
    published = PublishedManager() #自定义管理器
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title




