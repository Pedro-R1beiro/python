# Importação do pandas e criação do dataframe

import pandas as pd

# dataframe = pd.Dataframe()
venda = {
    'data': ['15/02/2021', '16/02/2021'],
    'valor': [500, 300],
    'produto': ['feijao', 'arroz'],
    'qtd': [50, 70]
}

vendas_df = pd.DataFrame(venda)

print(vendas_df)