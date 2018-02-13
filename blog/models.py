from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    body   = models.TextField()
    date   = models.DateTimeField()

    def __str__(self):
        return self.titulo