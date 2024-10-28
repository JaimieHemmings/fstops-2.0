from django.shortcuts import render
from blog.models import Article
from portfolio.models import Portfolio

def index(request):
  """
  A view that will render the index.html template
  """
  articles = Article.objects.all().order_by('-date')[:2]
  portfolio_items = Portfolio.objects.all().order_by('-date')[:4]
  context={
    'nbar': 'home',
    'articles': articles,
    'portfolio_items': portfolio_items
  }
  return render(request, 'home/index.html', context)


def about(request):
  """
  A view that will render the index.html template
  """
  context={}
  return render(request, 'about/about.html', context)
