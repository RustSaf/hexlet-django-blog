from django.urls import path
# from .views import IndexArticleView
from hexlet_django_blog.article.views import IndexView


app_name = "article"
urlpatterns = [
#    path('<str:tags>/<int:article_id>/',
#        IndexArticleView.as_view(),
#        name='index'
#    ),
    path('',
        IndexView.as_view(),
        name='index_'
    ),
]