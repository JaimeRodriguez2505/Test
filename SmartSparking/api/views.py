from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from web.models import Empresa,Estacionamiento,Estado
from .serializers import(
    EmpresaSerializer,
    EstacionamientoSerializer,
    EstadoSerializer,
)
    
class IndexView(APIView):
    
    def get(self, request):
        lista_empresas = Empresa.objects.all()
        data = [{'id': empresa.id, 'nombre': empresa.nombre, 'correo': empresa.correo, 'clave': empresa.clave} for empresa in lista_empresas]
        return Response(data)
    
class EmpresaView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
class EmpresaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    lookup_url_kwarg = 'empresa_id'
    serializer_class = EmpresaSerializer

class EstacionamientoView(generics.ListCreateAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer
    
class EstacionamientoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estacionamiento.objects.all()
    lookup_url_kwarg = 'estacionamiento_id'
    serializer_class = EstacionamientoSerializer

class EstadoView(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
class EstadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    lookup_url_kwarg = 'estado_id'
    serializer_class = EstadoSerializer
    
