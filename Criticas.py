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

    def calcular_xini():
        xini = []
        for i in range (len(dataset)):
            resultado = dt[col1][i]*dt[col2][i]
            xini.append(resultado)
        return xini

    dataset["XiNi"] = calcular_xini()
    suma_xini = dataset["XiNi"].sum()
    suma_ni = dataset[col2].sum()

    #Redondeamos la media a la centesimas
    return round(suma_xini/suma_ni, 2)


print(calcular_media(dt, "Opinion", "Cantidad de Votantes"))



#plt.show()