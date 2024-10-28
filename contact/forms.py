from django import forms
from django.core.validators import EmailValidator
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        placeholders = {
            "name": "Name",
            "email": "Email",
            "message": "Leave your message"
        }

        for field in self.fields:
            self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].widget.attrs["required"] = True