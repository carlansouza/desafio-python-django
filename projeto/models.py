from django.db import models


# Create your models here.

class User(models.Model):
    
    username = models.EmailField()
    password = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.username

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    requisitos = models.TextField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    escolaridade = models.CharField(max_length=100)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

