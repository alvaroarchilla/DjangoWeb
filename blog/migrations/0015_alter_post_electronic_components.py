# Generated by Django 3.2.6 on 2023-03-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20220929_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='electronic_components',
            field=models.ManyToManyField(blank=True, to='blog.ElectronicComponent'),
        ),
    ]
