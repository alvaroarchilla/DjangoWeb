# Generated by Django 3.2.6 on 2022-03-05 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_post_subcategoriaprincial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subcategoriaprincial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subcategoria', to='blog.subcategoria'),
        ),
    ]