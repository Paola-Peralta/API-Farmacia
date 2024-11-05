from .settings import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']

DATABASES = {
    'default': {
       'ENGINE': 'mssql',  # Utilizamos el backend mssql-django
       'NAME': config('BD_NAME'), 
         'HOST': config('BD_HOST'),  # IP del servidor SQL Server
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Driver ODBC instalado
             'trusted_connection': 'yes',  # Habilita la autenticación de Windows
             'extra_params': 'TrustServerCertificate=yes',  # Útil si estás usando SSL sin un certificado de confianza
       },
     }
 }