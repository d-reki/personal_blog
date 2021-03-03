from django.urls import path, re_path
from . import views
from .uploads import upload_image

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name="register"),  # 注册
    path('person/', views.person_center, name="person"), # 个人中心
    path('edit_user/', views.edit_user, name="edit_user"), # 编辑用户信息
    path('person_article/', views.person_article, name="person_article"), # 查询当前登录用户已经发布的文章
    path('person_add_article/', views.person_add_article, name="person_add_article"),  # 添加文章

    re_path('^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload'),   # 富文本编辑器上传图片功能

    # path('del-article/', views.del_article, name="del_article"),
]