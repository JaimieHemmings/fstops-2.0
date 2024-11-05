from django.shortcuts import render
from blog.models import Article
from portfolio.models import Portfolio
from .models import Review, FAQ, AboutPage, Mosaic, IntroGrid
from django.shortcuts import get_object_or_404
from services.models import Service

def index(request):
  """
  A view that will render the index.html template
  """
  faq = FAQ.objects.all()
  intro_section = get_object_or_404(IntroGrid.objects.all()[:1])
  articles = Article.objects.all().order_by('-date')[:2]
  portfolio_items = Portfolio.objects.all().order_by('-date')[:4]
  reviews = Review.objects.all()
  services = Service.objects.all()
  mosaicobjects = Mosaic.objects.all()
  context={
    'faq': faq,
    'articles': articles,
    'portfolio_items': portfolio_items,
    'reviews': reviews,
    'services': services,
    'mosaicobjects': mosaicobjects,
    'intro_section': intro_section
  }
  return render(request, 'home/index.html', context)


def about(request):
  """
  A view that will render the index.html template
  """
  # get the latest AboutPage object
  content = get_object_or_404(AboutPage.objects.all()[:1])
  context={
    'content': content
  }
  return render(request, 'about/about.html', context)
