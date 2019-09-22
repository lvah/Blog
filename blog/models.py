from django.db import models
from datetime import datetime


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    """分类表"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签表"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
   博客表
   """
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文,我们使用了 TextField。
    body = models.TextField()
    # 这两个列分别表示文章的创建时间和最后一次修改时间,存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(default=datetime.now())
    modified_time = models.DateTimeField(default=datetime.now())
    # 文章摘要,可以没有文章摘要,但默认情况下 CharField 要求我们必须存入数据,否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)
    # on_delete=False在Django1.x版本默认是不级联删除的，可以不做设置.  Django2.x一定要自行指定.
    category = models.ForeignKey(Category, on_delete=False)
    # blank=True标签可以不做设置
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        # 反向生成url地址， url_for('index')
        # 去寻找detail这个函数对应的url地址是什么
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
