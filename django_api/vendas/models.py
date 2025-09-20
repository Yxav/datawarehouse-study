# vendas/models.py
from django.db import models

class Produto(models.Model):
    id_produto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    data = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.FloatField()
