
from django.urls import path, include
from projeto.views import home, cadastrar, cadastrar_usuario, logar_usuario, relatorio

    
urlpatterns = [
    path('', home, name='home'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('relatorio/', relatorio, name="relatorio"),
]
