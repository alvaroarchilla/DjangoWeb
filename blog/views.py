from django.db.models.fields import related
from django.shortcuts import render
from blog.models import Post, Categoria, Subcategoria


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
    posts=Post.objects.filter(subcategorias=2)
    return render(request, "blog/subcategoria.html", {"subcategoria":subcategoria,"posts":posts})

def post(request, post_id):
    post=Post.objects.get(id=post_id)
    subcategorias=post.subcategorias.all()
    relacionados=Post.objects.filter(subcategorias=2)
    return render(request, "blog/post.html", {"post":post, "relacionados":relacionados, "subcategorias":subcategorias})