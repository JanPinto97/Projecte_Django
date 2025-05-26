from django.contrib import admin
from .models import Autor, Post, Tag

admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Tag)