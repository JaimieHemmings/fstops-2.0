from django.db import models
import uuid

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
