from django.db import models
import uuid
from colorfield.fields import ColorField

# Reviews Model
class Review(models.Model):
  
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"articles/img/{filename}"
    
    img = models.ImageField(upload_to=get_path)
    name = models.CharField(max_length=30)
    association = models.CharField(max_length=30)
    review = models.TextField()
    snippet = models.TextField()

    def __str__(self):
        return self.name
    

class FAQ(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

class AboutPage(models.Model):
  
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"about/img/{filename}"
    
    
    intro = models.TextField()
    subtitle_one = models.CharField(max_length=120)
    text_one = models.TextField()
    body_one = models.TextField()
    body_two = models.TextField()
    body_image = models.ImageField(upload_to=get_path)
    body_three = models.TextField()
    subtitle_two = models.CharField(max_length=120)
    text_two = models.TextField()
    body_four = models.TextField()

    def __str__(self):
        return self.intro


class Mosaic(models.Model):
  
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"mosaic/img/{filename}" 
    
    img = models.ImageField(upload_to=get_path, default="default.jpg", blank=True, null=True)
    backgroundColor = ColorField(default='#FFFFFF')
    bigNum = models.CharField(max_length=5, blank=True, null=True)
    symbol = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=120, default='Title Text')
    text = models.TextField(null=True, blank=True)
    link_text = models.CharField(max_length=120, blank=True, null=True)
    link = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.title