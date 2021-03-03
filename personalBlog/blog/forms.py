from django import forms
from .models import Comment
# class CommentForm(forms.Form):
#     """创建留言框"""
#     text = forms.CharField(label="评论内容", widget=forms.Textarea(attrs={
#         'class': 'textarea is-radiusless is-shadowless', 'rows':6}))

class CommentForm(forms.ModelForm):
    """创建留言框"""
    content = forms.CharField(label="评论内容", widget=forms.Textarea(attrs={
        'class': 'textarea is-radiusless is-shadowless', 'rows':6}))

    class Meta:
        model = Comment
        fields = ['content']