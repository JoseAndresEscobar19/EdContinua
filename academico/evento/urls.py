from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('tipoConvenioAliado', TipoConvenioAliadoViewSet)
router.register('aliado', AliadoViewSet)
router.register('docente', DocenteViewSet)
router.register('unidadAula', UnidadAulaViewSet)
router.register('tipoAula', TipoAulaViewSet)
router.register('estadoAula', EstadoAulaViewSet)
router.register('aula', AulaViewSet)
router.register('evento', EventoViewSet)
router.register('calendarioEvento', CalendarioEventoViewSet)
router.register('co', CoViewSet)
router.register('pubEvento', PubEventoViewSet)

urlpatterns = [  
    #Evento
    path('api/event/',include(router.urls)),
    path('crear/',CrearEvento.as_view(), name = 'crearEvento'),
    path('listar/',ListarEvento.as_view(), name = 'listarEvento'),
    path('editar/<int:pk>',EditarEvento.as_view(), name = 'editarEvento'),
    path('eliminar/<int:pk>',EliminarEvento.as_view(), name = 'eliminarEvento'),
    path('detalle/<int:pk>',DetalleEvento.as_view(), name = 'detalleEvento'),
    #Aula
    path('crear/',CrearAula.as_view(), name = 'crearAula'),
    path('listar/',ListarAula.as_view(), name = 'listarAula'),
    path('editar/<int:pk>',EditarAula.as_view(), name = 'editarAula'),
    path('eliminar/<int:pk>',EliminarAula.as_view(), name = 'eliminarAula'),
    #Aula
    path('crear/',CrearAliado.as_view(), name = 'crearAliado'),
    path('listar/',ListarAliado.as_view(), name = 'listarAliado'),
    path('editar/<int:pk>',EditarAliado.as_view(), name = 'editarAliado'),
    path('eliminar/<int:pk>',EliminarAliado.as_view(), name = 'eliminarAliado'),
    #Dia
    path('crear/',DiaCrear.as_view(), name = 'crearDia'),
    path('listar/',ListarDia.as_view(), name = 'listarDia'),
    path('editar/<int:pk>',EditarDia.as_view(), name = 'editarDia'),
    path('eliminar/<int:pk>',EliminarDia.as_view(), name = 'eliminarDia'),
    #Pub
    path('crear/',CrearPub.as_view(), name = 'crearPub'),
    path('listar/',ListarPub.as_view(), name = 'listarPub'),
    path('detalle/<int:pk>',infoEvento.as_view(), name = 'detallePub'),

    path('getNameE/', loadEventoName),
    #--------Seccion de reportes------------
    path('EventoCriterio/', EventoPorCriterio, name='EventoCriterio'),
    path('EventosPorGenero/',eventos_ejecutados,name='EventosPorGenero'),
    path('Registro_asistencia_evento/',Registro_asistencia_evento.as_view(),name='Registro_asistencia_evento'),
    path('detalle_participante/',detalle_part,name='detalle_participante'),
    
]
