from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Autor, Tag

def index(request):
    # Agafem els 3 posts més recents
    recent_posts = Post.objects.select_related('autor').order_by('-date')[:3]
    return render(request, 'blog/index.html', {'recent_posts': recent_posts})

def post_list(request):
    # Agafem tots els posts
    posts = Post.objects.select_related('autor').order_by('-date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    # Busquem el post pel slug
    try:
        post = Post.objects.select_related('autor').get(slug=slug)
    except Post.DoesNotExist:
        return HttpResponse("Post no trobat", status=404)
    return render(request, 'blog/post_detail.html', {'post': post})

def autor_list(request):
    # Agafem tots els autors
    autors = Autor.objects.all()
    return render(request, 'blog/autor_list.html', {'autors': autors})

def autor_detail(request, autor_id):
    # Busquem l'autor per la id
    try:
        autor = Autor.objects.prefetch_related('posts').get(id=autor_id)
    except Autor.DoesNotExist:
        return HttpResponse("Autor no trobat", status=404)
    return render(request, 'blog/autor_detail.html', {'autor': autor})

def tag_list(request):
    # Agafem tots els tag
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_detail(request, slug):
    # Busquem el tag pel slug
    try:
        tag = Tag.objects.prefetch_related('posts').get(slug=slug)
    except Tag.DoesNotExist:
        return HttpResponse("Tag no trobat", status=404)
    return render(request, 'blog/tag_detail.html', {'tag': tag})