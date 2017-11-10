from django.db import models


# Create your models here.
STATUS_CHOICES=(
    ('checkout',u'已出版'),
    ('dai',u'待出版'),
    ('status',u'审核中'),
)

# Author
class Author(models.Model):
    first_name = models.CharField(max_length=32, verbose_name="名")
    last_name = models.CharField(max_length=32, verbose_name="姓")
    email = models.EmailField(verbose_name="邮箱")
    def __unicode__(self):
        return "{}--{}".format(self.first_name, self.last_name)

    class Meta:
        # 首页model汉化
        verbose_name = '作者'
        verbose_name_plural = '作者'
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="名称")
    address = models.CharField(max_length=64, unique=True, verbose_name="地址")
    city = models.CharField(max_length=32, verbose_name="城市")
    state_province = models.CharField(max_length=32, verbose_name="省份")
    country = models.CharField(max_length=32, verbose_name="国家")
    website = models.URLField(verbose_name="网址")
    def __unicode__(self):
        return "{}".format(self.name)

    class Meta:

        verbose_name = '出版社'
        verbose_name_plural = '出版社'

    def __str__(self):
        return self.name

# Book
class Book(models.Model):
    name=models.CharField(max_length=64, verbose_name="名称")
    authors=models.ManyToManyField(Author, verbose_name="作者")  #作者,多对多的关系
    publisher=models.ForeignKey(Publisher, verbose_name="出版社")  #出版社,外键管理到Publisher表
    publisher_date=models.DateField(auto_now_add=True, verbose_name="出版日期")
    publisher_state=models.CharField(max_length=20,choices=STATUS_CHOICES,default='checkout', verbose_name="状态") #出版状态,是一个可选框
    def __unicode__(self):
        return "{}--{}".format(self.name,self.publisher_date)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

    def __str__(self):
        return self.name
