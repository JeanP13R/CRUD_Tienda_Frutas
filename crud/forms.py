
from django import forms
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class crear_producto_form(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    imagen = forms.ImageField(required=False)
    stock = forms.IntegerField(min_value=0)
    
class crear_producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'stock']
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name' ,'email', 'password1', 'password2']
