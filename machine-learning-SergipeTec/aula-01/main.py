import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('frutas-class.csv', delimiter=',')

#print(df)

x = df[['Cor', 'Peso Médio (g)', 'Textura', 'Formato']]
y = df['Fruta']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(x_treino, y_treino)

nova_fruta = pd.DataFrame([[2, 150, 2, 1]], columns=['Cor', 'Peso Médio (g)', 'Textura', 'Formato'])
previsao_nova = modelo_arvore.predict(nova_fruta)
print(f'A fruta com as características informada é: {previsao_nova[0]}')