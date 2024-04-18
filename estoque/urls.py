from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.index, name='index'),#DONE
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),#DONE
    path('remover_produto/<int:pk>/', views.remover_produto, name='remover_produto'),#DONE
    path('modificar_produto/<int:pk>/', views.modificar_produto, name='modificar_produto'),#DONE
    path('produtos_em_falta/', views.produtos_em_falta, name='produtos_em_falta'),#DONE
    path('produtos-existentes/', views.produtos_existentes, name='produtos_existentes')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)