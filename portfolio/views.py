from django.shortcuts import render
from .models import Portfolio
from django.core.paginator import Paginator


def portfolio(request):
  paginator = Paginator(Portfolio.objects.all().order_by("-date"), 6)
  page_num = request.GET.get("page")
  page_obj = paginator.get_page(page_num)
  context = {"page_obj": page_obj}
  return render(request, "portfolio.html", context)


def portfolio_item(request, slug):
  item = Portfolio.objects.get(slug=slug)
  last_three_items = Portfolio.objects.all().order_by("-date")[:3]
  context = {
    "item": item,
    "last_three_items": last_three_items
    }
  return render(request, "item.html", context)
