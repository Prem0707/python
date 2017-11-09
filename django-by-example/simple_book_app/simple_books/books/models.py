from django.db import models

# Create your models here.
STATUS_CHOICES=(
    ('checkout',u'已出版'),
    ('dai',u'待出版'),
    ('status',u'审核中'),
)

# Author
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    def __unicode__(self):
        return "{}--{}".format(self.first_name, self.last_name)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=32)
    state_province = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    website = models.URLField()
    def __unicode__(self):
        return "{}".format(self.name)
    def __str__(self):
        return self.name

# Book
class Book(models.Model):
    name=models.CharField(max_length=64)
    authors=models.ManyToManyField(Author)  #作者,多对多的关系
    publisher=models.ForeignKey(Publisher)  #出版社,外键管理到Publisher表
    publisher_date=models.DateField(auto_now_add=True)
    publisher_state=models.CharField(max_length=20,choices=STATUS_CHOICES,default='checkout') #出版状态,是一个可选框
    def __unicode__(self):
        return "{}--{}".format(self.name,self.publisher_date)
    def __str__(self):
        return self.name
