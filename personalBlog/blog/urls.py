from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^(?P<slug>[\w]+)/$', views.category, name='category'),
    path('article/<int:article_id>/', views.article, name="article"),
    path('comment/<int:article_id>/<int:comment_id>/', views.article, name="comment"),
    path('dates/<int:year>/<int:month>/', views.blog_get_dates, name="dates"),   # 归档页
    path('tags/<int:tag_id>/', views.blog_get_tags, name="tags"),      # 文章标签列表页
    path('search', views.search, name='search'),#搜索  


]