from django.db.models.fields import related
from django.shortcuts import render
from blog.models import Post, Categoria, PostSection, Subcategoria, CloudinaryMedia, ElectronicComponent, DeviceCategory


# Create your views here.
def blog(request):
    posts=Post.objects.all()
    categorias=Categoria.objects.all()
    return render(request, "blog/blog.html", {"posts":posts,"categorias": categorias})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request, "blog/categoria.html", {"categoria":categoria,"posts":posts})

def subcategoria(request, subcategoria_id):
    subcategoria=Subcategoria.objects.get(id=subcategoria_id)
    posts=Post.objects.filter(subcategorias=subcategoria_id)
    return render(request, "blog/subcategoria.html", {"subcategoria":subcategoria,"posts":posts})

def electronic_component(request):
    electronic_components=ElectronicComponent.objects.all()
    deviceCategories=DeviceCategory.objects.all()
    return render(request, "blog/electronic_component.html", {"electronic_components":electronic_components,"deviceCategories":deviceCategories})


def componentCategory(request, componentCategory_id):
    componentCategory=DeviceCategory.objects.get(id=componentCategory_id)
    electronicComponents=ElectronicComponent.objects.filter(deviceCategories=componentCategory)
    return render(request, "blog/componentCategory.html", {"componentCategory":componentCategory,"electronicComponents":electronicComponents})

def post(request, post_id):
    post=Post.objects.get(id=post_id)
    subcategoria=Post.related_post(post)
    relacionados=Post.objects.filter(subcategorias=post.subcategoriaprincial)
   # postSections=PostSection.objects.all()
    postSections=PostSection.objects.filter(relatedPost=post_id)
    return render(request, "blog/post.html", {"post":post,"postSections":postSections, "relacionados":relacionados, "subcategorias":subcategoria})

def galeriaCloudinary(request):
    cloudinarymedias=CloudinaryMedia.objects.all()
    return render(request, "blog/galeria.html", {"cloudinarymedias":cloudinarymedias})

