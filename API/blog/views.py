from django.shortcuts import render
from rest_framework import generics
from .serializer import ArticleSerializer
from .models import Article
# Create your views here.


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer