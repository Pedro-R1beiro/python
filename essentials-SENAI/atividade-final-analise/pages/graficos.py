import streamlit as st
import pandas as pd

data = pd.read_excel("xyz_enterprise.xlsx")

st.write('Salário Bruto vs Salário Líquido por funcionário:')
st.bar_chart(data[['Salário Líquido', 'Salário Bruto', 'Nome Completo']].set_index('Nome Completo'))

st.write('Total de Gratificação por Nível Funcional:')
st.bar_chart([data['Gratificação R$'].sum()])