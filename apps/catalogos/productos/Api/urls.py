from django.urls import path
from .views import ProductoApiView, ProductoDetails

app_name = "productos"
urlpatterns = [
    path('', ProductoApiView.as_view(), name = "productos"),
    path('<int:pk>/', ProductoDetails.as_view()),
]
