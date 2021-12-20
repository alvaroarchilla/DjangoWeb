# Generated by Django 3.2.6 on 2021-12-20 13:37

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_cloudinaryfiletest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cloudinaryfiletest',
            field=models.ImageField(blank=True, upload_to='test/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cloudinaryimg',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='/image/'),
        ),
    ]
