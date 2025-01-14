from django.urls import path
# from .views import IndexArticleView
from hexlet_django_blog.article.views import *


app_name = "articles"
urlpatterns = [
#    path('<str:tags>/<int:article_id>/',
#        IndexArticleView.as_view(),
#        name='index_'
#    ),
    path('',
        IndexView.as_view(),
        name='index'
    ),
    path('<int:id>/article_edit/',
         ArticleFormEditView.as_view(),
         name='article_update'
    ),
    path('<int:id>/delete/',
         ArticleFormDeleteView.as_view(),
         name='article_delete'),
    path('<int:id>/',
         ArticleView.as_view(),
         name='article_detail'
    ),
    path('article_create/',
         ArticleFormCreateView.as_view(),
         name='article_create'
    ),
    path('comment_create/<str:name>',
         CommentFormCreateView.as_view(),
         name='comment_create'
    ),
]