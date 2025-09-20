# vendas/views.py
from rest_framework import viewsets
import pandas as pd
from .models import Produto, Venda
from .serializers import ProdutoSerializer, VendaSerializer
import plotly.express as px
from django.shortcuts import render

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


def grafico_vendas(request):
    vendas = Venda.objects.all().values('data', 'valor_total', 'produto__nome')
    df = pd.DataFrame(vendas)
    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    df['mes'] = df['data'].dt.to_period('M').dt.to_timestamp()

    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    produto = request.GET.get('produto')

    if inicio:
        df = df[df['data'] >= pd.to_datetime(inicio)]
    if fim:
        df = df[df['data'] <= pd.to_datetime(fim)]
    if produto:
        df = df[df['produto__nome'] == produto]

    df_agg = df.groupby(['mes', 'produto__nome'])['valor_total'].sum().reset_index()

    fig = px.line(df_agg, x='mes', y='valor_total', color='produto__nome', title='Vendas Mensais por Produto',
                labels={'mes': 'Mês', 'valor_total': 'Valor Total', 'produto__nome': 'Produto'})
    grafico_html = fig.to_html(full_html=False)

    produtos = sorted(df['produto__nome'].unique())

    return render(request, 'grafico.html', {'grafico': grafico_html, 'produtos': produtos})
