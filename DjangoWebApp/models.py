from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import	RichTextField

# Create your models here.
class Bug(models.Model):
    priority= models.CharField(max_length=50, choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')])
    state= models.CharField(max_length=50, choices=[('Resuelto', 'Resuelto'), ('En proceso', 'En Proceso'), ('Planeado', 'Planeado')])
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    solution= RichTextField(blank=True, null=True)
    image=models.ImageField(upload_to="bug", null=True, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='bug'
        verbose_name_plural='bugs'
    
    def __str__(self):
        return self.title

