# Generated by Django 4.2.16 on 2024-11-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_post_excerpt'),
    ]
    operations = [
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]