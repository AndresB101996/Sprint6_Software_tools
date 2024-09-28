import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv("C:/Users/Andre/Documents/Andres/Self-learning/Bootcamp/Sprint6/Project/vehicles_us.csv") #read data


st.header('Sprint 6 Project: Software development tools') # Se crea el titulo de la pagina

st.dataframe(data=car_data) #Se muestra el dataframe

st.header('Histograma condicion vs modelo ') 



# Crear un filtro con selectbox
model_selected = st.selectbox('Condicion', car_data['condition'].unique())

# Filtrar el DataFrame basado en la categoría seleccionada
df_filtered = car_data[car_data['condition'] == model_selected]

#plot histogram
fig = px.histogram(df_filtered, x="model_year")
       
# interactive Plotly graph
st.plotly_chart(fig, use_container_width=True,)

build_histogram = st.checkbox('Histograma de kilometraje')
build_scatter = st.checkbox('Diagrama de dispersión precio vs kilometraje')


        
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


