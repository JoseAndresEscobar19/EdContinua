from django.urls import include, path
from rest_framework import routers
from academico.diseño_evento.views import *
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'area', AreaViewSet)
router.register(r'especialidad', EspecialidadViewSet)
router.register(r'tipoEvento', TipoEventoViewSet)
router.register(r'design', DesignEventoViewSet)
router.register(r'objetivoEspecifico', ObjetivoEspecificoViewSet)
router.register(r'unidad', UnidadViewSet)
router.register(r'subUnidad', SubUnidadViewSet)
router.register(r'recurso', RecursoViewSet)
router.register(r'lectura', LecturaViewSet)
router.register(r'referencia', ReferenciaViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('listar/',ListarAreaEspecialidad,name='listarGeneral'),
    #Area
    path('crear/',CrearArea.as_view(),name='crearArea'),
    path('editar/<int:pk>',UpdateArea.as_view(),name='updateArea'),
    #Especialidad
    path('crear/',CrearEspecialidad.as_view(),name='crearEspecialidad'),
    path('update/<int:pk>',UpdateEspecialidad.as_view(),name='updateEspecialidad'),
    #Design Evento
    path('listar/',ListarDesign.as_view(),name='listarDesign'),
    path('crear/',CrearDesign.as_view(),name='crearDesign'),
    #-----Seccion de reportes
    path('Eventos_Ejecutados/', eventos_ejecutados, name='Eventos_Ejecutados'),

]
