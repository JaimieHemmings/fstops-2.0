from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            
    context = {
        "form": form,
        "success": success
    }
    return render(request, "contact.html", context)
