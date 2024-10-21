import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos')

# Botón para construir un histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de vehículos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión de Odometer vs. Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
