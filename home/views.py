from django.shortcuts import render
from blog.models import Article
from portfolio.models import Portfolio
from .models import Review, FAQ

def index(request):
  """
  A view that will render the index.html template
  """
  faq = FAQ.objects.all()
  articles = Article.objects.all().order_by('-date')[:2]
  portfolio_items = Portfolio.objects.all().order_by('-date')[:4]
  reviews = Review.objects.all()
  context={
    'faq': faq,
    'articles': articles,
    'portfolio_items': portfolio_items,
    'reviews': reviews
  }
  return render(request, 'home/index.html', context)


def about(request):
  """
  A view that will render the index.html template
  """
  context={}
  return render(request, 'about/about.html', context)
