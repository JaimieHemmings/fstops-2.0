from django.db import models
import uuid


class Service(models.Model):
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"services/img/{filename}"
    
    name = models.CharField(max_length=100, null=False, blank=False)
    quote = models.CharField(max_length=180, null=False, blank=False)
    description = models.TextField()
    secondary_text = models.TextField()
    details_title = models.CharField(max_length=100, null=False, blank=False)
    details_description = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=get_path, null=False, blank=False)
    background_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    details_one_title = models.CharField(max_length=100, null=False, blank=False)
    details_one_description = models.CharField(max_length=100, null=False, blank=False)
    details_one_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    details_two_title = models.CharField(max_length=100, null=False, blank=False)
    details_two_description = models.CharField(max_length=100, null=False, blank=False)
    details_two_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    details_three_title = models.CharField(max_length=100, null=False, blank=False)
    details_three_description = models.CharField(max_length=100, null=False, blank=False)
    details_three_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    details_four_title = models.CharField(max_length=100, null=False, blank=False)
    details_four_description = models.CharField(max_length=100, null=False, blank=False)
    details_four_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    details_five_title = models.CharField(max_length=100, null=False, blank=False)
    details_five_description = models.CharField(max_length=100, null=False, blank=False)
    details_five_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    details_six_title = models.CharField(max_length=100, null=False, blank=False)
    details_six_description = models.CharField(max_length=100, null=False, blank=False)
    details_six_image = models.ImageField(upload_to=get_path, null=False, blank=False)
    cta_img = models.ImageField(upload_to=get_path, default='default.jpg')
    accreditation_img = models.ImageField(upload_to=get_path, default='default.jpg', null=True, blank=True)

    def __str__(self):
        return self.name
