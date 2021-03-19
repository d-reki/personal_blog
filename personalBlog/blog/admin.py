# from django.contrib import admin
# from .models import Category, Article, Tags, Comment   # 引入菜单模型类
# # Register your models here.

# admin.site.register(Category)   # 注册菜单类
# # admin.site.register(Article)   # 注册文章类
# admin.site.register(Tags)   # 注册文章标签类

# admin.site.register(Comment)   # 注册留言管理类

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     '''Admin View for Article'''
#     class Media:
#         js = (
#             'kindeditor/themes/default/default.css',
#             'kindeditor/themes/simple/simple.css',
#             'kindeditor/kindeditor-all-min.js',
#             'kindeditor/zh-CN.js',
#             'kindeditor/config.js',
            
#         )
#     # list_display = ('',)
#     # list_filter = ('',)
#     # inlines = [
#     #     Inline,
#     # ]
#     # raw_id_fields = ('',)
#     # readonly_fields = ('',)
#     # search_fields = ('',)
#     # date_hierarchy = ''
#     # ordering = ('',)
from django.contrib import admin
from django.apps import apps
from openpyxl import Workbook 
from django.http import HttpResponse
admin.site.site_title = '后台站点'
admin.site.site_header = 'my_blog'
# admin.site.index_title = '内容管理'
class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta # 用于定义文件名, 格式为: app名.模型类名
        field_names = [field.name for field in meta.fields]  # 模型所有字段名
        response = HttpResponse(content_type='application/msexcel') # 定义响应内容类型
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx' # 定义响应数据格式
        wb = Workbook()  # 新建Workbook
        ws = wb.active # 使用当前活动的Sheet表
        ws.append(field_names) # 将模型字段名作为标题写入第一行
        for obj in queryset: # 遍历选择的对象列表
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]  # 将模型属性值的文本格式组成列表
            row = ws.append(data) # 写入模型属性值
        wb.save(response) # 将数据存入响应内容
        return response
    export_as_excel.short_description = '导出Excel'

class ListAdminMixin(ExportExcelMixin):
    def __init__(self,model,admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.search_fields = [field.name for field in model._meta.fields]
        # self.list_filter = [field.name for field in model._meta.fields] 过滤器
        self.actions = ['export_as_excel']
        super(ListAdminMixin,self).__init__(model,admin_site)
models = apps.get_models()
for model in models:
    admin_class = type('AdminClass',(ListAdminMixin,admin.ModelAdmin),{})
    try:
        admin.site.register(model,admin_class)
    except admin.sites.AlreadyRegistered:
        pass

