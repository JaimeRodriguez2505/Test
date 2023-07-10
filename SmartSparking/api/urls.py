from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('empresa/',views.EmpresaView.as_view()),
    path('empresa/<int:empresa_id>',views.EmpresaDetailView.as_view()),
    path('estacionamiento/',views.EstacionamientoView.as_view()),
    path('estacionamiento/<int:estacionamiento_id>',views.EstacionamientoDetailView.as_view()),
    path('estado/',views.EstadoView.as_view()),
    path('estado/<int:estado_id>',views.EstadoDetailView.as_view()),
    
]