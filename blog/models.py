from django.db import models
from django.utils.text import slugify

class Autor(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nom} {self.cognom}"

class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)