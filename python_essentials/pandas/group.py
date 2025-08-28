# CALCULAR INDICADORES

import pandas as pd

vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')

# - value counts
""" transacoes_loja = vendas_df['ID Loja'].value_counts()
print(transacoes_loja) """

# - groupby
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum(numeric_only=True)
print(faturamento_produto)