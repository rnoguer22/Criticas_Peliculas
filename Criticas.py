import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Opinion":[5,4,3,2,1,0],
    "Cantidad de Votantes":[42,96,132,124,88,58]
}

#Creamos el dataframe a partir de los datos del enunciado
dt = pd.DataFrame(datos)
print (dt)

#Realizamos el grafico barras a partir de los datos del enunciado
dt.groupby("Opinion")["Cantidad de Votantes"].sum().plot(kind="bar")
#Añadimos un titulo para el grafico
plt.title("Opiniones obtenidas para una pelicula")
plt.show()

