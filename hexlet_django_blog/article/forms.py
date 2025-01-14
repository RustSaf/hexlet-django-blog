from django import forms # Импортируем формы Django
from django.forms import ModelForm
from .models import Article, ArticleComment


class ArticleForm(ModelForm):
    name = forms.CharField(max_length=100, label="Название")
    body = forms.CharField(widget=forms.Textarea(attrs={'colls': 60, 'rows': 10}), label="Содержание статьи")

    class Meta:
        model = Article
        fields = ['id', 'name', 'body']


#class CommentArticleForm(forms.Form):
#    content = forms.CharField(label='Комментарий') # Текст комментария
class ArticleCommentForm(ModelForm):
    content = forms.CharField(label="Комментарий")

    class Meta:
        model = ArticleComment
        fields = ['id', 'content', 'article']