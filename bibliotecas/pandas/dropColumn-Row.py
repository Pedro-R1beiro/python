# EXCLUIR LINHAS E COLUNAS

import pandas as pd
vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
vendas_df.loc[:, 'Imposto'] = 0

vendas_df = vendas_df.drop('Imposto', axis=1) # eixo 1 exclui coluna
vendas_df = vendas_df.drop(0, axis=0) # eixo 0 exclui linha
print(vendas_df)