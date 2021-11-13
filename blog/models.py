from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import	RichTextField
# Create your models here.

class Categoria(models.Model):
    name=models.CharField(max_length=50,unique=True,  choices=[('Electrónica', 'Electrónica'), ('Desarrollo Web', 'Desarrollo Web'), ('DataScience & IA', 'DataScience & IA'), ('Impresión 3D', 'Impresión 3D'), ('Otros Posts', 'Otros Posts')])
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.name


class Subcategoria(models.Model):
    name=models.CharField(max_length=50,unique=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='subcategoria'
        verbose_name_plural='subcategorias'
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    body=RichTextField(blank=True, null=True)
    image=models.ImageField(upload_to="blog", null=True, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    subcategorias=models.ManyToManyField(Subcategoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.title
    
