import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Opinion":[5,4,3,2,1,0],
    "Cantidad de Votantes":[42,96,132,124,88,58]
}

#Creamos el dataframe a partir de los datos del enunciado
dt = pd.DataFrame(datos)

#Realizamos el grafico barras a partir de los datos del enunciado
dt.groupby("Opinion")["Cantidad de Votantes"].sum().plot(kind="bar")
#Añadimos un titulo para el grafico
plt.title("Opiniones obtenidas para una pelicula")
#Eliminamos la etiqueta de texto del eje x
plt.xlabel(None)


#Cambiamos la columna "Cantidad de Votantes" del pequeño dataset
dt["Cantidad de Votantes"] = [40, 99, 145, 133, 96, 40]

#A continuacion vamos a crear una nueva columna del dataset, para facilitar el calculo de la media
#Creamos una funcion que nos calcula la columna xini
def calcular_media(dataset, col1, col2):
    xini = []
    for i in range (len(dataset)):
        resultado = dt[col1][i]*dt[col2][i]
        xini.append(resultado)
    return xini




#plt.show()