# Generated by Django 4.2 on 2024-11-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_introgrid_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introgrid',
            name='lead',
        ),
        migrations.AddField(
            model_name='introgrid',
            name='cta_img_alt',
            field=models.CharField(default='CTA Image', max_length=120),
        ),
        migrations.AddField(
            model_name='introgrid',
            name='img_alt',
            field=models.CharField(default='Image', max_length=120),
        ),
    ]
