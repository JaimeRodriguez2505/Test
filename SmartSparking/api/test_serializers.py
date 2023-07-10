from django.test import TestCase
from web.models import Empresa
from api.serializers import EmpresaSerializer
import re
from rest_framework.exceptions import ValidationError
import datetime


class EmpresaSerializerTest(TestCase):
    def test_serialization(self):
        empresa_data = {
            'nombre': 'Empresa 1',
            'correo': 'empresa1@example.com',
            'clave': 'secreta',
            'capacidad': 10
        }
        serializer = EmpresaSerializer(data=empresa_data)
        self.assertTrue(serializer.is_valid())
        empresa = serializer.save()
        self.assertEqual(empresa.nombre, empresa_data['nombre'])
        self.assertEqual(empresa.correo, empresa_data['correo'])
        self.assertEqual(empresa.clave, empresa_data['clave'])
        self.assertEqual(empresa.capacidad, empresa_data['capacidad'])

    def test_deserialization(self):
        empresa = Empresa.objects.create(nombre='Empresa 2', correo='empresa2@example.com', clave='secreta', capacidad=5)
        serializer = EmpresaSerializer(instance=empresa)
        data = serializer.data
        self.assertEqual(data['nombre'], empresa.nombre)
        self.assertEqual(data['correo'], empresa.correo)
        self.assertEqual(data['clave'], empresa.clave)
        self.assertEqual(data['capacidad'], empresa.capacidad)

    def test_invalid_data(self):
        empresa_data = {
            'nombre': 'Empresa 3',
            'correo': 'empresa3@example.com',
            'clave': '',  # Clave vacía (no válida)
            'capacidad': 20
        }
        serializer = EmpresaSerializer(data=empresa_data)
        self.assertFalse(serializer.is_valid())

    def test_update_instance(self):
        empresa = Empresa.objects.create(nombre='Empresa 4', correo='empresa4@example.com', clave='secreta', capacidad=15)
        new_data = {
            'nombre': 'Empresa Actualizada',
            'correo': 'nuevo_correo@example.com',
            'clave': 'nuevaclave',
            'capacidad': 30
        }
        serializer = EmpresaSerializer(instance=empresa, data=new_data)
        self.assertTrue(serializer.is_valid())
        updated_empresa = serializer.save()
        self.assertEqual(updated_empresa.nombre, new_data['nombre'])
        self.assertEqual(updated_empresa.correo, new_data['correo'])
        self.assertEqual(updated_empresa.clave, new_data['clave'])
        self.assertEqual(updated_empresa.capacidad, new_data['capacidad'])

    def test_partial_update_instance(self):
        empresa = Empresa.objects.create(nombre='Empresa 5', correo='empresa5@example.com', clave='secreta', capacidad=25)
        partial_data = {
            'capacidad': 40  # Solo se actualiza la capacidad
        }
        serializer = EmpresaSerializer(instance=empresa, data=partial_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_empresa = serializer.save()
        self.assertEqual(updated_empresa.nombre, empresa.nombre)
        self.assertEqual(updated_empresa.correo, empresa.correo)
        self.assertEqual(updated_empresa.clave, empresa.clave)
        self.assertEqual(updated_empresa.capacidad, partial_data['capacidad'])

 
class EmpresaModelTestCase(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(nombre='Mi Empresa', correo='empresa@example.com', clave='secreto', capacidad=10)

    def test_empresa_str(self):
        self.assertEqual(str(self.empresa), 'Empresa: Mi Empresa - Capacidad: 10')
        


def test_negative_capacity(self):
    empresa_data = {
        'nombre': 'Empresa 6',
        'correo': 'empresa6@example.com',
        'clave': 'secreta',
        'capacidad': -5  # Capacidad negativa (no válida)
    }
    serializer = EmpresaSerializer(data=empresa_data)
    self.assertFalse(serializer.is_valid())

def test_unique_email(self):
    empresa1 = Empresa.objects.create(nombre='Empresa 7', correo='empresa7@example.com', clave='secreta', capacidad=10)
    empresa_data = {
        'nombre': 'Empresa 8',
        'correo': 'empresa7@example.com',  # Mismo correo que empresa1 (no válido)
        'clave': 'secreta',
        'capacidad': 15
    }
    serializer = EmpresaSerializer(data=empresa_data)
    self.assertFalse(serializer.is_valid())

def test_fields_in_serialized_data(self):
    empresa = Empresa.objects.create(nombre='Empresa 9', correo='empresa9@example.com', clave='secreta', capacidad=10)
    serializer = EmpresaSerializer(instance=empresa)
    data = serializer.data
    self.assertEqual(set(data.keys()), {'nombre', 'correo', 'capacidad'})  # Solo se deben incluir estos campos
    
def test_min_length_nombre(self):
    empresa_data = {
        'nombre': 'A',  # Nombre demasiado corto (no válido)
        'correo': 'empresa10@example.com',
        'clave': 'secreta',
        'capacidad': 20
    }
    serializer = EmpresaSerializer(data=empresa_data)
    self.assertFalse(serializer.is_valid())


def test_partial_update_instance(self):
    empresa = Empresa.objects.create(nombre='Empresa 11', correo='empresa11@example.com', clave='secreta', capacidad=25)
    partial_data = {
        'correo': 'nuevo_correo@example.com'  # Solo se actualiza el correo
    }
    serializer = EmpresaSerializer(instance=empresa, data=partial_data, partial=True)
    self.assertTrue(serializer.is_valid())
    updated_empresa = serializer.save()
    self.assertEqual(updated_empresa.nombre, empresa.nombre)  # El nombre no se ha modificado
    self.assertEqual(updated_empresa.correo, partial_data['correo'])  # El correo se ha actualizado
    self.assertEqual(updated_empresa.clave, empresa.clave)  # La clave no se ha modificado
    self.assertEqual(updated_empresa.capacidad, empresa.capacidad)  # La capacidad no se ha modificado



def test_valid_email_format(self):
    empresa_data = {
        'nombre': 'Empresa 12',
        'correo': 'correo_invalido',  # Formato de correo no válido
        'clave': 'secreta',
        'capacidad': 30
    }
    serializer = EmpresaSerializer(data=empresa_data)
    self.assertFalse(serializer.is_valid())
    errors = serializer.errors
    self.assertTrue('correo' in errors)
    self.assertTrue(re.match(r'^Enter a valid email address\.$', str(errors['correo'][0])))

def test_exclude_password_field(self):
    empresa = Empresa.objects.create(nombre='Empresa 13', correo='empresa13@example.com', clave='secreta', capacidad=10)
    serializer = EmpresaSerializer(instance=empresa)
    data = serializer.data
    self.assertFalse('clave' in data)



def test_required_nombre_field(self):
    empresa_data = {
        'correo': 'empresa14@example.com',
        'clave': 'secreta',
        'capacidad': 40
    }
    serializer = EmpresaSerializer(data=empresa_data)
    with self.assertRaises(ValidationError):
        serializer.is_valid(raise_exception=True)

def test_serialization_multiple_objects(self):
    Empresa.objects.create(nombre='Empresa 15', correo='empresa15@example.com', clave='secreta', capacidad=10)
    Empresa.objects.create(nombre='Empresa 16', correo='empresa16@example.com', clave='secreta', capacidad=20)
    serializer = EmpresaSerializer(Empresa.objects.all(), many=True)
    data = serializer.data
    self.assertEqual(len(data), 2)  # Se esperan 2 objetos en la lista

def test_exclude_foreignkey_field(self):
    empresa = Empresa.objects.create(nombre='Empresa 18', correo='empresa18@example.com', clave='secreta', capacidad=10)
    estacionamiento = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    serializer = EstacionamientoSerializer(instance=estacionamiento)
    data = serializer.data
    self.assertFalse('id_empresa' in data)
    
def test_invalid_estacionamiento_deserialization(self):
    estacionamiento_data = {
        'id_empresa': 1000,  # ID de empresa no existente
        'lugar': '',  # Lugar vacío (no válido)
        'estado': True
    }
    serializer = EstacionamientoSerializer(data=estacionamiento_data)
    self.assertFalse(serializer.is_valid())
    errors = serializer.errors
    self.assertTrue('id_empresa' in errors)
    self.assertTrue('lugar' in errors)
    
def test_exclude_hora_salida_field(self):
    empresa = Empresa.objects.create(nombre='Empresa 19', correo='empresa19@example.com', clave='secreta', capacidad=10)
    estacionamiento = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    estado = Estado.objects.create(id_estacionamiento=estacionamiento, hora_ingreso='10:00:00', hora_salida='00:00:00')
    serializer = EstadoSerializer(instance=estado)
    data = serializer.data
    self.assertFalse('hora_salida' in data)
    
import datetime

def test_hora_ingreso_future_datetime(self):
    now = datetime.datetime.now()
    empresa = Empresa.objects.create(nombre='Empresa 20', correo='empresa20@example.com', clave='secreta', capacidad=10)
    estacionamiento = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    estado_data = {
        'id_estacionamiento': estacionamiento.id,
        'hora_ingreso': now - datetime.timedelta(minutes=30)  # Hora de ingreso anterior a la hora actual (no válido)
    }
    serializer = EstadoSerializer(data=estado_data)
    self.assertFalse(serializer.is_valid())

def test_empty_nombre_field(self):
    empresa_data = {
        'nombre': '',  # Nombre vacío (no válido)
        'correo': 'empresa3@example.com',
        'clave': 'secreta',
        'capacidad': 20
    }
    serializer = EmpresaSerializer(data=empresa_data)
    self.assertFalse(serializer.is_valid())


def test_update_invalid_instance(self):
    empresa = Empresa.objects.create(nombre='Empresa 21', correo='empresa21@example.com', clave='secreta', capacidad=20)
    empresa_data = {
        'nombre': '',  # Nombre vacío (no válido)
        'correo': 'nuevo_correo@example.com',
        'clave': 'nuevaclave',
        'capacidad': 30
    }
    serializer = EmpresaSerializer(instance=empresa, data=empresa_data)
    self.assertFalse(serializer.is_valid())

def test_valid_nombre_length(self):
    empresa_data = {
        'nombre': 'Empresa con nombre largo' * 10,  # Nombre largo (válido)
        'correo': 'empresa30@example.com',
        'clave': 'secreta',
        'capacidad': 20
    }
    serializer = EmpresaSerializer(data=empresa_data)
    self.assertTrue(serializer.is_valid())

def test_exclude_capacidad_field(self):
    empresa = Empresa.objects.create(nombre='Empresa 31', correo='empresa31@example.com', clave='secreta', capacidad=10)
    serializer = EmpresaSerializer(instance=empresa)
    data = serializer.data
    self.assertFalse('capacidad' in data)

def test_required_correo_field(self):
    empresa_data = {
        'nombre': 'Empresa 32',
        'clave': 'secreta',
        'capacidad': 40
    }
    serializer = EmpresaSerializer(data=empresa_data)
    with self.assertRaises(ValidationError):
        serializer.is_valid(raise_exception=True)

def test_serialization_empty_queryset(self):
    serializer = EmpresaSerializer(Empresa.objects.none(), many=True)
    data = serializer.data
    self.assertEqual(len(data), 0)  # No se esperan objetos en la lista

def test_exclude_foreignkey_field(self):
    empresa = Empresa.objects.create(nombre='Empresa 34', correo='empresa34@example.com', clave='secreta', capacidad=10)
    estacionamiento = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    serializer = EstacionamientoSerializer(instance=estacionamiento)
    data = serializer.data
    self.assertFalse('id_empresa' in data)

def test_invalid_estacionamiento_data(self):
    estacionamiento_data = {
        'id_empresa': 1,
        'lugar': 'Lugar 1',
        'estado': 'Activo'  # Estado no booleano (no válido)
    }
    serializer = EstacionamientoSerializer(data=estacionamiento_data)
    self.assertFalse(serializer.is_valid())

def test_exclude_hora_ingreso_field(self):
    empresa = Empresa.objects.create(nombre='Empresa 36', correo='empresa36@example.com', clave='secreta', capacidad=10)
    estacionamiento = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    estado = Estado.objects.create(id_estacionamiento=estacionamiento, hora_ingreso='10:00:00', hora_salida='12:00:00')
    serializer = EstadoSerializer(instance=estado)
    data = serializer.data
    self.assertFalse('hora_ingreso' in data)

def test_hora_salida_past_datetime(self):
    now = datetime.datetime.now()
    empresa = Empresa.objects.create(nombre='Empresa 37', correo='empresa37@example.com', clave='secreta', capacidad=10)
    estacionamiento = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    estado_data = {
        'id_estacionamiento': estacionamiento.id,
        'hora_ingreso': now - datetime.timedelta(hours=2),
        'hora_salida': now - datetime.timedelta(hours=3)  # Hora de salida anterior a la hora de ingreso (no válido)
    }
    serializer = EstadoSerializer(data=estado_data)
    self.assertFalse(serializer.is_valid())

def test_unique_lugar(self):
    estacionamiento1 = Estacionamiento.objects.create(id_empresa=empresa, lugar='Lugar 1', estado=True)
    estacionamiento_data = {
        'id_empresa': 1,
        'lugar': 'Lugar 1'  # Mismo lugar que estacionamiento1 (no válido)
    }
    serializer = EstacionamientoSerializer(data=estacionamiento_data)
    self.assertFalse(serializer.is_valid())

def test_required_hora_ingreso_field(self):
    estacionamiento_data = {
        'id_empresa': 1,
        'lugar': 'Lugar 2',
        'estado': True
    }
    serializer = EstacionamientoSerializer(data=estacionamiento_data)
    with self.assertRaises(ValidationError):
        serializer.is_valid(raise_exception=True)
