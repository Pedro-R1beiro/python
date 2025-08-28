# ADICIONAR COLUNA

import pandas as pd

vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')

# a partir de uma coluna que existe
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05

# criar uma coluna com valor padrão
vendas_df.loc[:, 'Imposto'] = 0

# ADICIONAR LINHA

vendas_dez_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas - Dez.xlsx')
vendas_df = pd.concat([vendas_df, vendas_dez_df])

# EXCLUIR LINHAS E COLUNAS

vendas_df = vendas_df.drop('Imposto', axis=1) # eixo 1 exclui coluna
vendas_df = vendas_df.drop(0, axis=0) # eixo 0 exclui linha
print(vendas_df)