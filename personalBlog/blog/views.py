from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse
from django.utils import timezone
from django.core.cache import cache, caches  # 缓存框架
# Create your views here.
from .models import Category, Article, Tags, Comment       # 引入菜单模型类 
from .forms import CommentForm
from django.db.models import Q
def index(request):
    """首页函数，把首页想要显示的内容都在这里查询"""
    article_list = Article.objects.all()    # 查询到文章的所有数据，显示到首页
    context = {'article_list':article_list}  # 定义上下文
    return render(request, 'blog/index.html', context)


def category(request, slug):
    """获取当前分类，并查询到当前分类的所有文章"""
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category_list.html', locals())


def article(request, article_id):
    """获取文章详情"""
    article = get_object_or_404(Article, id=article_id)
    content_count = len(str(article.content))  # 统计文章字数

    # 获取上下篇
    per_article = Article.objects.filter(add_date__lt=article.add_date).last()
    next_article = Article.objects.filter(add_date__gt=article.add_date).first()
   
    # 判断是否为POST请求，如果不是
    if request.method != "POST":
        # 显示空表单
        form = CommentForm()
    else:
        # 否则显示空表单，并且获取表单输入的数据
        form = CommentForm(data=request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # 将表单中的数据暂存到内存
            new_article = form.save(commit=False)
            new_article.author = request.user
            # 表单模型关联的文章为我们已经获取到的当前文章的id，在最开始处
            new_article.article = article
            # 保存
            new_article.save()
            # 成功之后跳转回当前页
            return HttpResponseRedirect(reverse('blog:article', args=[article_id]))
    return render(request, 'blog/article.html', locals())


def blog_get_dates(request, year, month):
    """ 文章归档列表页 """
    blog_dates = Article.objects.filter(add_date__year=year, add_date__month=month)
    return render(request, 'blog/dates.html', locals())


def blog_get_tags(request, tag_id):
    """ 标签列表页 """
    tag = get_object_or_404(Tags, id=tag_id)
    return render(request, 'blog/tags.html', locals())

def search(request):
    search = request.GET.get('search')
    if search is not None:
        article_list = Article.objects.filter(Q(title__icontains=search) or Q(body__icontains=search))
    else:
        search = ''
        article_list = ArticlePost.objects.all()
    print('111',article_list)
    context = {'article_list':article_list}  # 定义上下文
    return render(request, 'blog/index.html', context)

