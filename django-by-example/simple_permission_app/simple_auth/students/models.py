from django.db import models
# Create your models here.
SEX_CHOICES = (
    ('female', '女'),
    ('man', '男')
)
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=20,choices=SEX_CHOICES,default='man', verbose_name="状态")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
        # 权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
        permissions = (
            ('views_student_list', '查看学员信息表'),
            ('views_student_info', '查看学员详细信息'),
        )