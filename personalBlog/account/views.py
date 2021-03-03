from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from blog.models import Article, Tags, Category
from .models import UserInfo
from .forms import RegisterForm, UserInfoForm, UserInfoRegisterForm, UserForm, ArticleForm   # 引入forms.py中定义好的表单类

def register(request):
    if request.method != "POST":
        # Django自带的User模型的表单
        form = RegisterForm()
        # 自己通过一对一创建的用户表单
        user_info_form = UserInfoRegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        user_info_form = UserInfoRegisterForm(data=request.POST)
        if form.is_valid() and user_info_form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password2'))
            new_user.save()
            new_user_info = user_info_form.save(commit=False)
            new_user_info.author = new_user
            new_user_info.save()
            return redirect('login')

    return render(request, 'registration/register.html', {'form':form, 'user_info_form':user_info_form})


@login_required(login_url='login')
def person_center(request):
    # 个人中心
    return render(request, 'account/person_center.html')


@login_required(login_url='login')
def edit_user(request):
    # 修改用户信息
    user = User.objects.get(username=request.user)  # 获取当前用户
    user_info = user.userinfo   # 一对一关系获取
    if request.method != "POST":
        # instance 用来设置以当前信息填充表单
        form = UserForm(instance=user)
        user_info_form = UserInfoForm(instance=user_info)
    else:
        # request.POST 用来获取表单中的文本数据  request.FILES 用来获取表单中上传的二进制文件数据
        user_info_form = UserInfoForm(request.POST, request.FILES, instance=user_info )
        form = UserForm(request.POST, instance=user)
        # 验证两个表单数据的合法性
        if user_info_form.is_valid() and form.is_valid():
            # 不使用表单获取字段的方式单独保存，我们直接保存模型
            user_info.save()
            user.save()
            return redirect('account:person')     # 保存成功跳转到个人中心主页
    return render(request, 'account/edit_user.html', locals())


@login_required(login_url='login')
def person_article(request):
    # 查询当前用户已经发布的文章
    article_list = Article.objects.filter(author=request.user).order_by('pub_date')
    return render(request, 'account/person_article.html', locals())


@login_required(login_url='login')
def person_add_article(request):
    # 添加文章
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    
    if request.method != 'POST':
        form = ArticleForm()
    else:
        # 创建表单，并获取表单中的数据
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 暂存数据，并返回一个类字典数据
            new_article = form.save(commit=False)
            # 将作者信息加入到这个类字典
            new_article.author = request.user
            new_article.content = request.POST.get('content')
            new_article.save()  # 保存
            # 获取多对多的tags文章标签，getlist()方法获取多选数据
            tags = request.POST.getlist('tags')
            # 获取到刚才创建的这篇文章
            b = Article.objects.get(id=new_article.id)
            # 使用set()方法将tags关联到文章
            b.tags.set(tags)
            form.save_m2m()  # 保存多对多数据
            return redirect('account:person_article')
    return render(request, 'account/person_add_article.html', locals())

# @login_required(login_url='login')
# @csrf_exempt
# def del_article(request):
#     article_id = request.POST['content']
#     try:
#         article = ArticlePost.objects.get(id=article_id)
#         article.delete()
#         return HttpResponse("1")
#     except:
#         return HttpResponse("2")
