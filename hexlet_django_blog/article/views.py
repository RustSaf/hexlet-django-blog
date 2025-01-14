from django.shortcuts import get_object_or_404, render, redirect
# from django.urls import reverse
from django.views import View
# from django.http import Http404

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.models import ArticleComment
from .forms import *

# class IndexArticleView(View):
#
#     def get(self, request, tags=None, article_id=None):
#         if tags and article_id:
#             return render(request, 'articles/index.html', context={
#                 'tags': tags, 'article_id': article_id
#             })
#         raise Http404()

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
#         try:
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        comments = ArticleComment.objects.all().order_by('-created_at')[:15]
#        comments = ArticleComment.objects.get('article')
#        print(comments)
#        comments_article = {}
#        for comment in comments: 
#            if comment.article == article:
#                comments_article = {**comments_article, **comment}
#                comment += comment.
#        print(comments_article)
#        comments = ArticleComment.objects.get('article.id').order_by('-created_at')[:15]
#        comments = ArticleComment.objects.select_related('article').order_by('-created_at')[:15]
        return render(request, 'articles/article.html', context={
            'article': article,
            'comments': [comments_article for comments_article in comments if comments_article.article == article],
#            'comments': comments_article,
        })
#        return render(request, 'articles/article.html', context={
#            'article': article
#        })
#         except Exception:
#             raise Http404()


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'articles/article_create.html', context={'form': form}) # Передаем нашу форму в контексте
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данные формы на корректность
            form.save() # Сохраняем форму
            return redirect('articles:index')
        return render(request, 'articles/article_create.html', context={'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/article_update.html', {'form': form, 'article_id':article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

        return render(request, 'articles/article_update.html', {'form': form, 'article_id':article_id})


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles:index')


class CommentFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm() # Создаем экземпляр нашей формы
        article_name = kwargs.get('name')
        return render(request, 'articles/comment_create.html', context={'form': form, 'name': article_name}) # Передаем нашу форму в контексте
    
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST) # Получаем данные формы из запроса
#        id = form['id']
#        self.cleaned_data['content']
#        art = form['article']        
#        comments = get_object_or_404(ArticleComment, article=art)
#        article_id = comments.article.id
#        article = get_object_or_404(Article, id=article_id)
#        article_id = comments.article.id
#        article = get_object_or_404(Article, article_id)
        if form.is_valid(): # Проверяем данные формы на корректность
#            article.comment.content = form.cleaned_data['content']
            form.save() # Сохраняем форму
#            return render(request, 'articles/article.html', context={
#                'article': article,
#                'comments': comments
#            })
            return redirect('articles:index')
        return render(request, 'articles/comment_create.html', context={'form': form})

#             comment = form.save(commit=False) # Получаем заполненную модель
             # Дополнительно обрабатываем модель
#             comment.content = check_for_spam(form.data['content'])

#             comment.save()
