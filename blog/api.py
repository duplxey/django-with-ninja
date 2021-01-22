from typing import List

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Router

from blog.models import Article
from blog.schemas import ArticleOut, ArticleIn

router = Router()


@router.get("/article/{article_id}", response=ArticleOut)
def get_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return article


@router.get("/article-list", response=List[ArticleOut])
def get_articles(request):
    articles = Article.objects.all()
    return articles


@router.post("/create-article")
def create_article(request, payload: ArticleIn):
    passed = payload.dict()
    try:
        author = User.objects.get(id=passed['author'])
        del passed['author']
        article = Article.objects.create(author=author, **passed)
        return {'detail': "The specific user cannot be found."}
    except User.DoesNotExist:
        return {'detail': "The specific user cannot be found."}

