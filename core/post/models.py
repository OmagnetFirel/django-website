from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Categoria(models.Model):
    title = models.CharField(max_length=45, null=False)
    slug = models.SlugField(unique=True, null=False )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Publicacao(models.Model):
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    title = models.CharField(max_length=45, null=False)
    slug = models.SlugField(unique=True, null=False)
    subtitle = models.CharField(max_length=155, null=False)
    description = models.TextField(max_length=255, null=False)
    image = models.ImageField(upload_to='images/', blank=True)
    text = RichTextUploadingField(config_name='awesome_ckeditor')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def image_table(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" width="50">'.format(self.image.url))
        else:
            return mark_safe('<p> Sem Imagem </p>')
        
        

class Comentario(models.Model):
    
    STATUS = (
        ('Lido', 'Lido'),
        ('Não Lido', 'Não Lido')
        ) 
        
    post = models.ForeignKey(Publicacao, on_delete=models.CASCADE, null=False)
     
    name = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=50,blank=False)
    comentario = models.TextField()
    status = models.CharField(choices=STATUS, max_length=10, default="Não Lido")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    