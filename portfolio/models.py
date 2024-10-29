from django.db import models
from django.template.defaultfilters import slugify
import uuid
import string  # for string constants
import random  # for generating random strings
from ckeditor.fields import RichTextField


class Portfolio(models.Model):

    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"articles/img/{filename}"
    

    def save(self, *args, **kwargs):
        # Check if the title has changed
        if self.pk is not None:
            # Fetch the existing object from the database
            existing_obj = Portfolio.objects.get(pk=self.pk)
            if existing_obj.title != self.title:
                self.slug = self.generate_slug()
        else:
            # New object, generate slug
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
    

    title = models.CharField(max_length=120)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=get_path)
    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    img_one = models.ImageField(upload_to=get_path)
    img_two = models.ImageField(upload_to=get_path)
    img_three = models.ImageField(upload_to=get_path)
    img_four = models.ImageField(upload_to=get_path)
    img_five = models.ImageField(upload_to=get_path)
    img_six = models.ImageField(upload_to=get_path)
    img_seven = models.ImageField(upload_to=get_path)
    img_eight = models.ImageField(upload_to=get_path)
    img_nine = models.ImageField(upload_to=get_path)
    img_ten = models.ImageField(upload_to=get_path)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


