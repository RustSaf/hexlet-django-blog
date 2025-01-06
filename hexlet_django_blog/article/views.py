from django.shortcuts import render
from django.views import View
# from django.http import Http404


from hexlet_django_blog.article.models import Article


#class IndexArticleView(View):
#
#    def get(self, request, tags=None, article_id=None):
#        if tags and article_id:
#            return render(request, 'articles/index.html', context={
#                'tags': tags, 'article_id': article_id
#            })
#        raise Http404()

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
