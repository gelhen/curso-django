from django.urls import path
from pypro.modulos import views


app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('', views.indice, name='indice'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
]
