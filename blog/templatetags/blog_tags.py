from django import template

from ..models import Post, Category

# 创建模板库对象
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    # print(Post.objects.dates)
    # print(Post.objects.dates('created_time', 'month', order='DESC'))
    return Post.objects.dates('created_time', 'month', order='DESC')
@register.simple_tag
def get_categories():
   # 别忘了在顶部引入 Category 类
   return Category.objects.all()