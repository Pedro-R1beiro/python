# PEGAR LINHAS

import pandas as pd

vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')

# pegar baseado em id
""" print(vendas_df.loc[1]) id 1
print(vendas_df.loc[1:5]) id 1-5 """

# pegar linhas correspondentes a uma condição
""" print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']) """

# pegar várias linhas e colunas usando loc
""" print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]) """

# pegar um valor específico
""" print(vendas_df.loc[1, 'Produto']) """