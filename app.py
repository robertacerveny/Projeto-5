import pandas as pd
import plotly.express as px
import streamlit as st

# carregar dados
car_data = pd.read_csv('C:/Users/rober/Downloads/vehicles.csv')

# título
st.header('Análise de anúncios de carros')

# checkbox histograma
build_histogram = st.checkbox('Criar histograma')

if build_histogram:
    st.write('Histograma da quilometragem dos veículos')

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

# checkbox scatter
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Relação entre preço e quilometragem')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig, use_container_width=True)