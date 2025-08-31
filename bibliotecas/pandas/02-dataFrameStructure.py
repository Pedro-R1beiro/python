import pandas as pd

vendas_df = pd.read_excel(r'C:\Users\pedro\Desktop\python\python_essentials\pandas\planilha\Vendas.xlsx')

""" print(vendas_df.head(10)) método para ver o início da tabela
print(vendas_df.shape) (n° de linhas, n° de colunas)
print(vendas_df.describe()) visão geral de como as informações estão """

# dataframe é uma tabela e cada coluna é uma series
# pegar colunas (series)

""" produtos = vendas_df[['Produto', 'ID Loja']]
print(produtos) """