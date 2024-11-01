# Generated by Django 4.2 on 2024-11-01 15:31

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField()),
                ('subtitle_one', models.CharField(max_length=120)),
                ('text_one', models.TextField()),
                ('body_one', models.TextField()),
                ('body_two', models.TextField()),
                ('body_image', models.ImageField(upload_to=home.models.AboutPage.get_path)),
                ('body_three', models.TextField()),
                ('subtitle_two', models.CharField(max_length=120)),
                ('text_two', models.TextField()),
                ('body_four', models.TextField()),
            ],
        ),
    ]