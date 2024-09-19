from django.db import models


class Categoria(models.Model): 
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=200)
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='images/')
    stock = models.IntegerField(default=0)
    # categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=200)
    email = models.EmailField()
    contraseña = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    roles = models.ManyToManyField('Rol')