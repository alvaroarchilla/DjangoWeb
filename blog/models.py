from turtle import title
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import	RichTextField
from cloudinary.models import CloudinaryField
from django.db.models import query

#from blog.admin import PostSectionAdmin


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

class CloudinaryFile(models.Model):
    name=models.CharField(auto_created=True, max_length=50,unique=True)
    cloudinaryfile= CloudinaryField('Imagen',blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
        
    class Meta:
        verbose_name='cloudinaryfile'
        verbose_name_plural='cloudinaryfiles'
    
    def __str__(self):
        return self.name
    
class DeviceCategory(models.Model):
    deviceCategoryName=models.CharField(auto_created=True, max_length=50,unique=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
        
    class Meta:
        verbose_name='DeviceCategory'
        verbose_name_plural='DeviceCategories'
    
    def __str__(self):
        return self.deviceCategoryName
        
class ElectronicComponent(models.Model):
    deviceName=models.CharField(max_length=50,unique=True)
    deviceType=models.CharField(max_length=50,  choices=[('Sensores', 'Sensores'), ('Actuadores', 'Actuadores'), ('Componentes', 'Componentes'), ('Microcontroladores', 'Microcontroladores')])
    deviceDescription=models.CharField(max_length=500,blank=True, null=True)
    deviceCategories=models.ManyToManyField(DeviceCategory)
    workingVoltage=models.FloatField(blank=True, null=True)
    workingCurrent=models.FloatField(blank=True, null=True)
    cloudinaryimg= CloudinaryField('image',blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='ElectronicComponent'
        verbose_name_plural='ElectronicComponents'
        
    def __str__(self):
        return self.deviceName

class Post(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    cloudinaryimg= CloudinaryField('image',blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    subcategorias=models.ManyToManyField(Subcategoria)
    subcategoriaprincial= models.ForeignKey(Subcategoria,on_delete=models.DO_NOTHING,  null=True,  related_name="Subcategoria")
    electronic_components=models.ManyToManyField(ElectronicComponent,blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    def related_post(self):

        return self.categorias
    
    def __str__(self):
        return self.title
       

class PostSection(models.Model):
    relatedPost=models.ForeignKey(Post,  null=True, on_delete=models.CASCADE)
    sectionTitle=models.CharField(max_length=50, blank=True, null=True)
    title=models.CharField(max_length=50)
    body1=RichTextField(blank=True, null=True)
    cloudinaryimg1= CloudinaryField('image',blank=True)
    body2=RichTextField(blank=True, null=True)
    cloudinaryimg2= CloudinaryField('image',blank=True)
    body3=RichTextField(blank=True, null=True)
    cloudinaryimg3= CloudinaryField('image',blank=True)
    body4=RichTextField(blank=True, null=True)
    cloudinaryimg4= CloudinaryField('image',blank=True)
    body5=RichTextField(blank=True, null=True)
    cloudinaryimg5= CloudinaryField('image',blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='postSection'
        verbose_name_plural='postSections'
        
    def __str__(self):
        return '%s - %s - %s' % ( self.relatedPost,self.pk,self.title )    
    
class CloudinaryMedia(models.Model):
    name=models.CharField(max_length=50,unique=True)
    body=RichTextField(blank=True, null=True)
    name2=models.ManyToManyField(Subcategoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    #image = CloudinaryJsFileField(attrs = { 'multiple': 1 })
    relatedpost=models.ManyToManyField(Post)
    cloudinaryfiles = models.ManyToManyField('CloudinaryFile',blank=True)
   # cloudinaryfiletest= models.ImageField(upload_to='https://api.cloudinary.com/v1_1/dpc0ldfnt/mh/upload',blank=True)


    class Meta:
        verbose_name='cloudinaryMedia'
        verbose_name_plural='cloudinaryMedias'
    
    def __str__(self):
        return self.name






