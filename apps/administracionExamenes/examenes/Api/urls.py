from django.urls import path, include
from apps.administracionExamenes.examenes.Api.views import ExamenApiView, ExamenDetails

app_name = 'compras'
urlpatterns = [
    path('', ExamenApiView.as_view(), name='compras'),
    path('<int:pk>/', ExamenDetails.as_view()),
]