from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto, Categoria, Rol, Usuario
from .forms import crear_producto_form, CustomUserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout , authenticate , login
from django.contrib import messages
from .decorators import group_required

def home(request):
    productos= Producto.objects.all()
    return render(request,'home.html',{'productos':productos})


@login_required(redirect_field_name="siguiente")
def crud_productos(request):
    if request.method == 'POST' and request.POST.get('action') == 'delete':
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, idProducto=producto_id)
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('crud_productos')
    productos= Producto.objects.all()
    return render(request,'index.html',{'productos':productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = crear_producto_form(request.POST, request.FILES)  # Añade request.FILES para manejar la imagen
        if form.is_valid():
            Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                imagen=form.cleaned_data['imagen'],
                stock=form.cleaned_data['stock'],
                
            )
            return redirect('crud_productos')
    else:
        form = crear_producto_form  
    
    return render(request, 'crear_producto.html', {'form': form})


def actualizar_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    
    if request.method == 'POST':
        form = crear_producto_form(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crud_productos')
    else:
        form = crear_producto_form(instance=producto)
    
    return render(request, 'actualizar_producto.html', {'form': form, 'producto': producto})

def exit(request):
    logout(request)
    return redirect('home')

#no funciona
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            # Guarda al usuario
            user_creation_form.save()

            # Autentica al usuario
            username = user_creation_form.cleaned_data['username']
            password = user_creation_form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)  # Inicia sesión
                messages.success(request, "Se registró correctamente.")
                return redirect('home')  # Redirige al home
            else:
                messages.error(request, "Error al autenticar al usuario.")
        else:
            # Si el formulario no es válido, reenviamos el formulario con errores
            data['form'] = user_creation_form  # Pasa el formulario con errores al contexto
    
    return render(request, 'registration/register.html', data)


#cuenta admin:
#jeanpier
#correo123


