from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.CharField(max_length=120)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade_em_estoque = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    #estoque_minimo = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.produto

class MinhaImagem(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.titulo  # Corrigido para retornar self.titulo ao invés de self.produto

@receiver(post_delete, sender=Estoque)
def delete_image_on_product_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem when corresponding `Estoque` object is deleted.
    """
    if instance.imagem:
        instance.imagem.delete(save=False)

class MinhaImagem(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')


    