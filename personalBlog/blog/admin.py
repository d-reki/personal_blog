from django.contrib import admin
from .models import Category, Article, Tags, Comment   # 引入菜单模型类
# Register your models here.

admin.site.register(Category)   # 注册菜单类
# admin.site.register(Article)   # 注册文章类
admin.site.register(Tags)   # 注册文章标签类

admin.site.register(Comment)   # 注册留言管理类

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Admin View for Article'''
    class Media:
        js = (
            'kindeditor/themes/default/default.css',
            'kindeditor/themes/simple/simple.css',
            'kindeditor/kindeditor-all-min.js',
            'kindeditor/zh-CN.js',
            'kindeditor/config.js',
            
        )
    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
