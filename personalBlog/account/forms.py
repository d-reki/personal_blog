from django import forms
from django.contrib.auth.models import User
from .models import UserInfo
from blog.models import Article
import re


class CKEditorWidget(forms.Textarea):
    class Media:
        css = {

        }
        js = (
           'https://cdn.ckeditor.com/ckeditor5/12.3.1/classic/ckeditor.js',
           'ckeditor/config.js',
        )

class KindEditorWidget(forms.Textarea):
    class Media:
        css = {'all': (
                'kindeditor/themes/default/default.css',
                'kindeditor/themes/simple/simple.css',
                )}
        js = (
            'kindeditor/kindeditor-all-min.js',
            'kindeditor/zh-CN.js',
            'kindeditor/config.js',         
        )

class RegisterForm(forms.ModelForm):
    """Form definition for Register."""
    username = forms.CharField(label="用户名", widget=forms.TextInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))
    email = forms.CharField(label="邮箱", widget=forms.EmailInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))
    password2 = forms.CharField(label="再次输入密码", widget=forms.PasswordInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))

    class Meta:
        """Meta definition for Registerform."""
        model = User
        fields = ('username','email')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("您输入的两次密码不一致！")
        return password2


class UserInfoRegisterForm(forms.ModelForm):
    """Form definition for UserInfo."""
    phone = forms.CharField(label="手机号", widget=forms.TextInput(
        attrs={'class':'input is-radiusless is-shadowless'}
    ))

    class Meta:
        """Meta definition for UserInfoform."""

        model = UserInfo
        fields = ('phone',)

    def clean_phone(self):
        # 对手机号进行验证
        phone = self.cleaned_data.get('phone')
        regex = re.compile(r'^1[^012]\d{9}$')
        if regex.search(phone) == None:
            raise forms.ValidationError('请输入正确的手机号码！')
        return phone



class UserInfoForm(forms.ModelForm):
    """Form definition for UserInfo."""
    user_desc = forms.CharField(label="个性签名", widget=forms.TextInput(
        attrs={'class':'input'}
    ))
    user_content = forms.CharField(label="个人介绍", widget=forms.Textarea(
        attrs={'class':'textarea'}
    ))
    phone = forms.CharField(label="手机号", widget=forms.TextInput(
        attrs={'class':'input'}
    ))

    class Meta:
        """Meta definition for UserInfoform."""

        model = UserInfo
        fields = ('phone','user_img', 'user_desc', 'user_content',  'user_type')


class UserForm(forms.ModelForm):
    """Form definition for Register."""
    email = forms.CharField(label="邮箱", widget=forms.EmailInput(
        attrs={'class':'input'}
    ))

    class Meta:
        """Meta definition for Registerform."""
        model = User
        fields = ('email',)



class ArticleForm(forms.ModelForm):
    """Form definition for Article."""
    title = forms.CharField(label="文章标题", 
        widget=forms.TextInput(attrs={'class':'input'}))
    desc = forms.CharField(label="文章描述", widget=forms.Textarea(
        attrs={'class':'textarea', 'rows':4}
    ))
    content = forms.CharField(label="文章内容", widget=KindEditorWidget)

    class Meta:
        """Meta definition for Articleform."""

        model = Article
        exclude = ['author',]
