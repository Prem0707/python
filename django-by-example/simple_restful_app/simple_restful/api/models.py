from django.db import models

class Task(models.Model):
    title = models.CharField('标题', max_length=100)
    description = models.CharField('描述', max_length=300)
    completed = models.BooleanField('是否完成', default=False)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
