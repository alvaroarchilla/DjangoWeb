# Generated by Django 3.2.6 on 2022-03-05 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_cloudinaryfile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcategoriaprincial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subcategoria', to='blog.subcategoria'),
        ),
    ]
