# Generated by Django 4.2 on 2024-10-28 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_category_slug_alter_portfolio_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
