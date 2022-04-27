import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

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

#Mostramos el resultado por pantalla
media = calcular_media(dt, "Opinion", "Cantidad de Votantes")
print(media)


#Ahora vamos a hacer lo mismo pero para calcular la desviacion tipica
def calcular_std(dataset, col1, col2):

    def columna_std():
        columna = []
        media = calcular_media(dataset, col1, col2)
        for i in range(len(dataset)):
            resultado = dataset[col2][i] * (dataset[col1][i] - media)*(dataset[col1][i] - media)
            columna.append(resultado)
        return columna

    dataset["Ni*((Xi-media)^2)"] = columna_std()
    suma_columna = dataset["Ni*((Xi-media)^2)"].sum()
    suma_ni = dataset[col2].sum()
    varianza = suma_columna/suma_ni

    return round(sqrt(varianza),2)

std = calcular_std(dt, "Opinion", "Cantidad de Votantes")
print (std)

def porcentaje(dataset, col1, col2, num):
    lim_inf = media - num*std
    lim_sup = media + num*std
    print([lim_inf, lim_sup])
    r = []
    s = []
    for i in range (len(dataset)):
        if dt[col1][5-i] >= lim_inf and dt[col1][5-i] <= lim_sup:
            r.append(dataset[col1][i])
            s.append(dt[col2][i])
        else:
            pass

    r.sort()
    print (r)

    #Hallamos el porcentaje a ver si es correcto
    print ("El porcentaje es {}%".format(round(sum(s)/dt["Cantidad de Votantes"].sum(), 2)))
    #Esto es correcto ya que con [1,2,3] el porcentaje se queda por debajo de 67%, buscamos que se quede minimo por encima de 68%

porcentaje (dt, "Opinion", "Cantidad de Votantes", 1.1)

#plt.show()