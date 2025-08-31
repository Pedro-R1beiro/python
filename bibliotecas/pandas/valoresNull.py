# TRATAR VALORES VAZIOS

import pandas as pd

vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')

vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
vendas_dez_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas - Dez.xlsx')
vendas_df = pd.concat([vendas_df, vendas_dez_df])

# deletar linhas e colunas completamente vazia
""" vendas_df = vendas_df.dropna(how='all') """ # exclui todas a linhas em que todos os valores são vazios
""" vendas_df = vendas_df.dropna(how='all', axios=1) """ # exclui todas as colunas em que todos os valores são vazios

# deletar linhas linhas que possuem pelo menos um valor vazio
# vendas_df = vendas_df.dropna() # exclui todas as linhas em que tem ao menos um valor vazio

# preencher valores vazios

# com a média da coluna
# vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) # preenche com a média do coluna Comissão

# preencher com o último valor
vendas_df = vendas_df.ffill()
print(vendas_df)