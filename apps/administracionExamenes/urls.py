from django.urls import path, include

urlpatterns = [
    path('examenes/', include('apps.administracionExamenes.examenes.Api.urls')),
    path('consultas/', include('apps.administracionExamenes.consultas.Api.urls')),
    path('detalleExamen/', include('apps.administracionExamenes.detalleExamen.Api.urls')),
]
