# Generated by Django 4.2 on 2024-10-29 09:40

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quote', models.CharField(max_length=180)),
                ('description', models.TextField()),
                ('secondary_text', models.TextField()),
                ('details_title', models.CharField(max_length=100)),
                ('details_description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('background_image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('details_one_title', models.CharField(max_length=100)),
                ('details_one_description', models.CharField(max_length=100)),
                ('details_one_image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('details_two_title', models.CharField(max_length=100)),
                ('details_two_description', models.CharField(max_length=100)),
                ('details_two_image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('details_three_title', models.CharField(max_length=100)),
                ('details_three_description', models.CharField(max_length=100)),
                ('details_three_image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('details_four_title', models.CharField(max_length=100)),
                ('details_four_description', models.CharField(max_length=100)),
                ('details_four_image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('details_five_title', models.CharField(max_length=100)),
                ('details_five_description', models.CharField(max_length=100)),
                ('details_five_image', models.ImageField(upload_to=services.models.Service.get_path)),
                ('details_six_title', models.CharField(max_length=100)),
                ('details_six_description', models.CharField(max_length=100)),
                ('details_six_image', models.ImageField(upload_to=services.models.Service.get_path)),
            ],
        ),
    ]
