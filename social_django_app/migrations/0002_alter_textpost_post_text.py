# Generated by Django 5.0.6 on 2024-06-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_django_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpost',
            name='post_text',
            field=models.CharField(max_length=280),
        ),
    ]
