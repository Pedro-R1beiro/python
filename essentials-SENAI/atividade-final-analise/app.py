import streamlit as st
import pandas as pd

# Carregar o Excel
data = pd.read_excel("xyz_enterprise.xlsx")

st.title("Análise: Folha de Pagamento - XYZ Enterprise")

questionList = [
    '',
    'Quantos funcionários a empresa possui?',
    'Qual o salário líquido médio, o maior e o menor?',
    'Qual o valor total gasto com gratificações e horas extras?',
    'Qual funcionário (nome) recebeu a maior gratificação e qual recebeu a menor?',
    'Qual funcionário paga o maior imposto de renda e qual paga o menor?',
    'Qual funcionário tem o maior salário líquido e qual tem o menor?'
]

questionSelect = st.selectbox('Selecione a pergunta que deseja responder:', questionList)

if questionSelect == 'Quantos funcionários a empresa possui?':
    st.write(f'Número de funcionários: {data['Nome Completo'].nunique()}')

if questionSelect == 'Qual o salário líquido médio, o maior e o menor?':
    st.write(f'Média salário líquido: R$ {data['Salário Líquido'].min():.2f}')
    st.write(f'Maior salário líquido: R$ {data['Salário Líquido'].max():.2f}')
    st.write(f'Menor salário líquido: R$ {data['Salário Líquido'].mean():.2f}')

if questionSelect == 'Qual o valor total gasto com gratificações e horas extras?':
    st.write(f'Gastos com gratificações e horas extras: R$ {(data['Gratificação R$'].sum() + data['Hora Extra (Total.)'].sum()):,.2f}')
    
if questionSelect == 'Qual funcionário (nome) recebeu a maior gratificação e qual recebeu a menor?':
    st.write('Funcionário(s) com maior gratificação: ')
    st.write(data.loc[data['Gratificação R$'] == data['Gratificação R$'].max()][['Nome Completo', 'Gratificação R$']])
    
    st.write('Funcionário(s) com menor gratificação: ')
    st.write(data.loc[data['Gratificação R$'] == data['Gratificação R$'].min()][['Nome Completo', 'Gratificação R$']])
    
if questionSelect == 'Qual funcionário paga o maior imposto de renda e qual paga o menor?':
    st.write('Funcionário(s) que paga maior imposto de renda: ')
    st.write(data.loc[data['Imposto de Renda R$'] == data['Imposto de Renda R$'].max()][['Nome Completo', 'Imposto de Renda R$']])
    
    st.write('Funcionário(s) que paga menor imposto de renda: ')
    st.write(data.loc[data['Imposto de Renda R$'] == data['Imposto de Renda R$'].min()][['Nome Completo', 'Imposto de Renda R$']])
    
if questionSelect == 'Qual funcionário tem o maior salário líquido e qual tem o menor?':
    st.write('Funcionário(s) com maior salário líquido: ')
    st.write(data.loc[data['Salário Líquido'] == data['Salário Líquido'].max()][['Nome Completo', 'Salário Líquido']])
    
    st.write('Funcionário(s) com menor salário líquido: ')
    st.write(data.loc[data['Salário Líquido'] == data['Salário Líquido'].min()][['Nome Completo', 'Salário Líquido']])
    
st.bar_chart(data[['Salário Líquido', 'Salário Bruto', 'Nome Completo']].set_index('Nome Completo'))
st.bar_chart([data['Gratificação R$'].sum(), data['Nível Funcional'].sum()])