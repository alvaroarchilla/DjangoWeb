from django.db.models.fields import related
from django.shortcuts import render
from blog.models import Post, Categoria, Subcategoria, CloudinaryMedia


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

def post(request, post_id):
    post=Post.objects.get(id=post_id)
    subcategoria=Post.related_post(post)
    relacionados=Post.objects.filter(subcategorias=post.subcategoriaprincial)
    return render(request, "blog/post.html", {"post":post, "relacionados":relacionados, "subcategorias":subcategoria})

def galeriaCloudinary(request):
    cloudinarymedias=CloudinaryMedia.objects.all()
    return render(request, "blog/galeria.html", {"cloudinarymedias":cloudinarymedias})