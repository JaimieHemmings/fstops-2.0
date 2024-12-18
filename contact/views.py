from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

            # Send an email to the Admin alerting them of a new message
            send_mail(
                "FStops: New Contact Form Submission",
                "A new contact form submission has been made at www.fstops.co.uk.",
                "jwarbz@gmail.com",
                ["benniw8@gmail.com"],
                fail_silently=False,
            )
            
    context = {
        "form": form,
        "success": success
    }
    return render(request, "contact.html", context)
