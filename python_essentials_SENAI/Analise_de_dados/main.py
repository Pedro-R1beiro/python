import streamlit as st
import pandas as pd
import os

os.system('cls')

data = pd.read_excel('base_mercado.xlsx')

st.title('Gráfico de Produtos')
st.subheader('Análise dos Principais Notebooks')
st.write('Quantidade Empresa: ', data['FABRICANTE'].nunique())

manufacturers = st.multiselect('Escolha uma opção', data['FABRICANTE'].unique())

col1, col2 = st.columns(2)

if manufacturers:
    total = 0
    for i in manufacturers:
        new_data = data.loc[data['FABRICANTE'] == i]
        total += new_data['RECEITA BRUTA'].sum()
    with col1:
        st.metric('Total: ', f'R$ {total:,.2f}')
    with col2:
        st.metric('Média: ', f'R$ {total/len(manufacturers):,.2f}')
else:
    with col1:
        st.metric('Total: ', f'R$ {data['RECEITA BRUTA'].sum():,.2f}')
    with col2:
        st.metric('Média: ', f'R$ {data['RECEITA BRUTA'].mean():,.2f}')

with st.popover('Show Details'):
    for manufacturer in manufacturers:
        new_data = data.loc[data['FABRICANTE'] == manufacturer]
        total += new_data['RECEITA BRUTA'].sum()

        st.metric(f'Total da receita bruta {manufacturer}: ', f'R$ {new_data['RECEITA BRUTA'].sum():,.2f}')

st.bar_chart(data.groupby('FABRICANTE')['RECEITA BRUTA'].sum())