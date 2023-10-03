from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo= models.CharField(max_length=50)
    autor= models.CharField(max_length=30)
    abstract=models.TextField()
    
    def __str__(self):
        return f'{self.titulo} {self.autor} {self.abstract}'


    