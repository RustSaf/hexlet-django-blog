from django.db import models
#from .models_comment import ArticleComment


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class ArticleComment(models.Model):
    content = models.CharField('comment', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Статьи")







