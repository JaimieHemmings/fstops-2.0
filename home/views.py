from django.shortcuts import render

def index(request):
  """
  A view that will render the index.html template
  """
  context={}
  return render(request, 'home/index.html', context)


def about(request):
  """
  A view that will render the index.html template
  """
  context={}
  return render(request, 'about/about.html', context)
