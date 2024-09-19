from django.contrib import admin
from django.urls import  path
from crud import views

urlpatterns = [
    path("", views.home , name="home"),
    path('crear', views.crud_productos, name='crud_productos'),
    path('crear_producto', views.crear_producto, name='crear_producto'),
    path('actualizar_producto/<int:idProducto>/', views.actualizar_producto, name='actualizar_producto'),
    path('exit', views.exit, name='exit'),
    path('register', views.register, name='register'),
]