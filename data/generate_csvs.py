import pandas as pd
import random
from datetime import datetime, timedelta

# Criar lista de produtos
produtos = [
    {"id_produto": 1, "nome": "Smartphone", "categoria": "Eletrônicos"},
    {"id_produto": 2, "nome": "Camiseta", "categoria": "Roupas"},
    {"id_produto": 3, "nome": "Arroz", "categoria": "Alimentos"},
    {"id_produto": 4, "nome": "Notebook", "categoria": "Eletrônicos"},
    {"id_produto": 5, "nome": "Tênis", "categoria": "Roupas"},
    {"id_produto": 6, "nome": "Café", "categoria": "Alimentos"},
    {"id_produto": 7, "nome": "Fone de ouvido", "categoria": "Eletrônicos"},
    {"id_produto": 8, "nome": "Jaqueta", "categoria": "Roupas"},
]

# Gerar produtos.csv
df_produtos = pd.DataFrame(produtos)
df_produtos.to_csv("data/produtos.csv", index=False)

# Gerar vendas.csv
vendas = []
for i in range(1, 201):  # 200 vendas
    produto = random.choice(produtos)
    quantidade = random.randint(1, 10)
    valor_unitario = round(random.uniform(20, 3000), 2)
    data = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    vendas.append({
        "id_venda": i,
        "data": data.strftime("%Y-%m-%d"),
        "id_produto": produto["id_produto"],
        "quantidade": quantidade,
        "valor_total": round(quantidade * valor_unitario, 2)
    })

df_vendas = pd.DataFrame(vendas)
df_vendas.to_csv("data/vendas.csv", index=False)

print("Arquivos produtos.csv e vendas.csv gerados com sucesso!")
