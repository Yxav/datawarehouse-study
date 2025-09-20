import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

produtos = pd.read_csv('data/produtos.csv')
vendas = pd.read_csv('data/vendas.csv')

vendas.rename(columns={'id_produto': 'produto_id'}, inplace=True)

produtos.to_sql('vendas_produto', engine, if_exists='replace', index=False)
vendas.to_sql('vendas_venda', engine, if_exists='replace', index=False)
