# Generated by Django 4.2 on 2024-10-30 11:51

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_cta_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='accreditation_img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=services.models.Service.get_path),
        ),
    ]
