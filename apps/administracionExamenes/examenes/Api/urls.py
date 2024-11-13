from django.urls import path, include
from apps.administracionExamenes.examenes.Api.views import ExamenApiView, ExamenDetails

app_name = 'examenes'
urlpatterns = [
    path('', ExamenApiView.as_view(), name='examenes'),
    path('<int:pk>/', ExamenDetails.as_view()),
]