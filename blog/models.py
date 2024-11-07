from django.db import models
from django.template.defaultfilters import slugify
import uuid
import string  # for string constants
import random  # for generating random strings
import datetime
from ckeditor.fields import RichTextField


class Article(models.Model):
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"articles/img/{filename}"
  
    meta_description = models.CharField(max_length=155, null=False, blank=False, default='This is the default meta description')
    title = models.CharField(max_length=120)
    thumbnail = models.ImageField(upload_to=get_path)
    slug = models.SlugField(null=True, blank=True, unique=True)
    date = models.DateField(("Date"), default=datetime.date.today)
    intro = models.TextField(default="This is the intro")
    lead_paragraph = models.TextField(default="This is the lead paragraph")
    body = RichTextField()
    body_img = models.ImageField(upload_to=get_path)

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super().save(*args, **kwargs)
  
    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
        generated_slug = slugify(self.title)
      
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        
        return generated_slug
  
def __str__(self):
    return self.title


