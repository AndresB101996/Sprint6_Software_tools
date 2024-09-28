import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("C:/Users/Andre/Documents/Andres/Self-learning/Bootcamp/Sprint6/Project/vehicles_us.csv") #read data
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un diagrama de dispersión')


st.header('Sprint 6 Project: Software development tools')
        
if build_histogram: # mark the check box
    # Write a message
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    #plot histogram
    fig = px.histogram(car_data, x="odometer")
        
    # interactive Plotly graph
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    # Write a message
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    #plot histogram
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # interactive Plotly graph
    st.plotly_chart(fig, use_container_width=True)


