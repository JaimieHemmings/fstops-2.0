# Generated by Django 4.2 on 2024-11-04 10:13

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_service_accreditation_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='homepage_description',
            field=models.CharField(default='This is the default decription', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='homepage_img',
            field=models.ImageField(default='default.jpg', upload_to=services.models.Service.get_path),
        ),
    ]