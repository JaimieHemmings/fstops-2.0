from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
