# Generated by Django 3.2.10 on 2021-12-19 15:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20211219_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_likes',
            field=models.ManyToManyField(blank=True, related_name='post_image_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
