from django.contrib import admin

# Register your models here.
from academico.evento.models import CalendarioEvento,TipoConvenioAliado, Aliado, Docente, UnidadAula, TipoAula, EstadoAula, Aula,Evento

#admin.site.register(TipoEvento)
#admin.site.register(Modalidad)
admin.site.register(TipoConvenioAliado)
admin.site.register(Aliado)
admin.site.register(Docente)
admin.site.register(UnidadAula)
admin.site.register(TipoAula)
admin.site.register(EstadoAula)
admin.site.register(Aula)
admin.site.register(CalendarioEvento)
#admin.site.register(Publico)
#admin.site.register(Servicio)
admin.site.register(Evento)
