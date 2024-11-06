import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el conjunto de datos en un DataFrame
data = pd.read_csv("vehicles_us.csv")  # Asegúrate de que el archivo esté en el mismo directorio

# Encabezado de la aplicación
st.header("Cuadro de Mandos de Análisis de Vehículos")

# Casilla de verificación para el histograma
if st.checkbox("Mostrar Histograma de Precios"):
    fig_hist = px.histogram(data, x="price", nbins=30, title="Distribución de Precios de Vehículos")
    st.plotly_chart(fig_hist)  # Muestra el histograma en Streamlit

# Casilla de verificación para el gráfico de líneas
if st.checkbox("Mostrar Gráfico de Líneas de Precio Promedio por Año"):
    # Calcula el precio promedio por año del modelo
    avg_price_by_year = data.groupby("model_year")["price"].mean().reset_index()
    fig_line = px.line(avg_price_by_year, x="model_year", y="price", title="Precio Promedio por Año del Modelo",
                       labels={"model_year": "Año del Modelo", "price": "Precio Promedio"})
    st.plotly_chart(fig_line)  # Muestra el gráfico de líneas en Streamlit

# Visualización rápida de los datos (opcional)
st.write("Vista previa del conjunto de datos:")
st.write(data.head())

