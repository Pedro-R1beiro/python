# MESCLAR TABELAS

import pandas as pd

vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')

gerentes_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Gerentes.xlsx')

vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)