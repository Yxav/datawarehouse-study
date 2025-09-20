# vendas/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, VendaViewSet, grafico_vendas

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('grafico/', grafico_vendas, name='grafico_vendas'),
]
