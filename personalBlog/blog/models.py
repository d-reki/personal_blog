from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """博客分类模型."""
    name = models.CharField('分类名称', max_length=50)    # 标题字段
    slug = models.SlugField(max_length=50)   # Slug是一个报纸术语。SlugField表示定义短标签，只包含字母，数字，下划线或连字符，通常用于URL。
    desc = models.TextField('分类描述')  # 内容字段，用于存储大段文本
    add_date = models.DateTimeField('发布日期', auto_now_add=True)  
    # DateTimeField时间字段，当设置 auto_now_add=True ,当你首次发布信息时自动保存你首次发布的时间。
    # 当设置 auto_now=True ,那么在每次修改信息时都将自动保存为当前日期时间
    pub_date = models.DateTimeField('修改日期', auto_now=True)


    class Meta:
        """Meta definition for Category."""

        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Tags(models.Model):
    """文章标签"""
    tag = models.CharField('文章标签', max_length=20, help_text='文章标签')
    add_date = models.DateTimeField('发布日期', auto_now_add=True)
    pub_date = models.DateTimeField('修改日期', auto_now=True)

    class Meta :
        ordering = ['-tag']
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Article(models.Model):
    """博客文章模型."""
    title = models.CharField('文章标题', max_length=68)
    # 多对一关联字段ForeignKey，将多篇文章关联到某一个指定分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    # 关联到某一个作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_related', verbose_name="作者")
    desc = models.TextField('文章描述', max_length=200, blank=True, default='')
    content = models.TextField('文章内容')
    tags = models.ManyToManyField(Tags, verbose_name="文章标签")
    add_date = models.DateTimeField('发布日期', auto_now_add=True)
    pub_date = models.DateTimeField('修改日期', auto_now=True)

    class Meta:
        """Meta definition for Article."""
        ordering = ['-add_date']
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        """Unicode representation of Article."""
        return self.title


class Comment(models.Model):
    """评论管理"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")
    content = models.CharField('评论内容', max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者") 
    add_date = models.DateTimeField('评论日期', auto_now_add=True)
    pub_date = models.DateTimeField('修改日期', auto_now=True)
    
    class Meta:
        """Meta definition for Comment."""

        verbose_name = '评论管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        """Unicode representation of Comment."""
        return self.content
