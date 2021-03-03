from django import template
from django.utils.safestring import mark_safe
from blog.models import Category, Comment, Article, Tags

# 这里的register不能随便修改
register = template.Library()

@register.simple_tag
def get_category_list():   # 可以定义任意名称函
    return Category.objects.all()


@register.simple_tag
def get_comment_list():   # 可以定义任意名称函
    return Comment.objects.order_by('-add_date')[:5]


@register.simple_tag
def get_month_list():     # 按月份进行匹配归档
    return Article.objects.dates('add_date', 'month', order='DESC')

@register.simple_tag
def get_tags_list():     # 侧边栏显示所有标签
    return Tags.objects.all()