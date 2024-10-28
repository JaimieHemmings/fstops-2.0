from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article


def blog(request):
  paginator = Paginator(Article.objects.all(), 8)
  page_num = request.GET.get("page")
  page_obj = paginator.get_page(page_num)
  context = {"page_obj": page_obj}
  return render(request, "blog/blog.html", context)


def article(request, slug):
  article = Article.objects.get(slug=slug)
  last_three_articles = Article.objects.all().order_by("-date")[:3]
  context = {
    "article": article,
    "last_three_articles": last_three_articles
    }
  return render(request, "blog/article.html", context)