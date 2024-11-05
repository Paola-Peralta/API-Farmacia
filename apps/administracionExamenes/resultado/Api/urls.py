from django.urls import path, include
from apps.administracionExamenes.resultado.Api.views import ResultadoApiView, ResultadoDetails

app_name = 'resultado'
urlpatterns = [
    path('', ResultadoApiView.as_view(), name='resultado'),
    path('<int:pk>/', ResultadoDetails.as_view()),
]