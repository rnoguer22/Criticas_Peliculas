# Criticas_Peliculas

[Pinshe aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Criticas_Peliculas.git)

---

*Queda resuelta la tarea Criticas Peliculas de Estructura de datos y algoritmos I. Para ello, hemos introducido todo el codigo en un archivo de python, a modo de apuntes, para explicar todo lo propuesto en la tarea, pero usando el lenguaje de programacion Python. Posteriormente, hemos generalizado dicho codigo, para poder reutilizarlo con cualquier dataset, utilizando la programacion orientada a objetos de python POO.*

---

## Indice
* [Apuntes](#1)
### Clases
* [grafico](#2)
* [media](#3)
* [std](#4)
* [porcentaje](#5)
* [main](#6)

---

## Apuntes.py<a name="1"></a>
```Python3
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
            resultado = dataset[col1][i]*dataset[col2][i]
            xini.append(resultado)
        return xini

    dataset["XiNi"] = calcular_xini()
    suma_xini = dataset["XiNi"].sum()
    suma_ni = dataset[col2].sum()

    #Redondeamos la media a la centesimas
    return suma_xini/suma_ni

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

    return sqrt(varianza)

std = calcular_std(dt, "Opinion", "Cantidad de Votantes")
print (std)

def porcentaje(dataset, col1, col2, num):
    lim_inf = media - num*std
    lim_sup = media + num*std
    r = []
    s = []
    for i in range (len(dataset)):
        if dt[col1][len(dataset)-1-i] >= lim_inf and dt[col1][len(dataset)-1-i] <= lim_sup:
            r.append(dataset[col1][i])
            s.append(dt[col2][i])
        else:
            pass
    r.sort()
    print (r)

    #Hallamos el porcentaje
    print ("El porcentaje es {}%".format(round(sum(s)/dt["Cantidad de Votantes"].sum(), 2)))



porcentaje (dt, "Opinion", "Cantidad de Votantes", 1)
porcentaje (dt, "Opinion", "Cantidad de Votantes", 2)
porcentaje (dt, "Opinion", "Cantidad de Votantes", 3)

#Podemos ver que estos porcentajes no son correctos. Esto es debido a que el dataset es demsasiado
#pequeño, por lo que no es correcto la aproximacion a la normal

plt.show()
```

---

## Clases
### grafico.py<a name="2"></a>
```Python3
from Clases.media import Media
import matplotlib.pyplot as plt

class Grafico(Media):
    #Constructor
    def __init__(self, dataset, col1, col2):
        super().__init__(dataset, col1, col2)
    
    def grafico_barras(self, title):
        self.dataset.groupby(self.col1)[self.col2].sum().plot(kind="bar")
        plt.title(title)
        plt.xlabel(None)
        plt.show()
```

---

### media.py<a name="3"></a>
```Python3
class Media:
    #Constructor
    def __init__(self, dataset, col1, col2):
        self.dataset = dataset
        self.col1 = col1
        self.col2 = col2

    def calcular_media(self):

        def calcular_xini():
            xini = []
            for i in range (len(self.dataset)):
                resultado = self.dataset[self.col1][i]*self.dataset[self.col2][i]
                xini.append(resultado)
            return xini

        self.dataset["XiNi"] = calcular_xini()
        suma_xini = self.dataset["XiNi"].sum()
        suma_ni = self.dataset[self.col2].sum()

        return suma_xini/suma_ni
```

---

### std.py<a name="4"></a>
```Python3
from media import Media
from math import sqrt

class Std(Media):
    #Constructor
    def __init__(self, dataset, col1, col2):
        #Heredamos el constructor de la clase Media
        super().__init__(dataset, col1, col2)

    def calcular_std(self):

        def columna_std():
            columna = []
            media = self.calcular_media()
            for i in range(len(self.dataset)):
                resultado = self.dataset[self.col2][i] * (self.dataset[self.col1][i] - media)*(self.dataset[self.col1][i] - media)
                columna.append(resultado)
            return columna

        self.dataset["Ni*((Xi-media)^2)"] = columna_std()
        suma_columna = self.dataset["Ni*((Xi-media)^2)"].sum()
        suma_ni = self.dataset[self.col2].sum()
        varianza = suma_columna/suma_ni

        return sqrt(varianza)
```

---

### porcentaje.py<a name="5"></a>
```Python3
from media import Media
from std import Std
import pandas as pd

class Porcentaje(Media):
    #Constructor
    def __init__(self, dataset, col1, col2):
        #Heredamos el constructor de la clase Media
        super().__init__(dataset, col1, col2)
        self.media = Media(dataset, col1, col2)
        self.desviacion = Std(dataset, col1, col2)

    def porcentaje(self, num):
        lim_inf = self.media.calcular_media() - num*self.desviacion.calcular_std()
        lim_sup = self.media.calcular_media() + num*self.desviacion.calcular_std()
        r = []
        s = []
        indice = len(self.dataset) - 1
        for i in range (len(self.dataset)):
            if self.dataset[self.col1][indice-i] >= lim_inf and self.dataset[self.col1][indice-i] <= lim_sup:
                r.append(self.dataset[self.col1][i])
                s.append(self.dataset[self.col2][i])
            else:
                pass
        r.sort()
        print (r)

        #Hallamos el porcentaje
        return (round(sum(s)/self.dataset[self.col2].sum(), 2))
```

---

### main.py<a name="6"></a>
```Python3
import pandas as pd
from grafico import Grafico
from media import Media
from std import Std
from porcentaje import Porcentaje


if __name__ == '__main__':
    #El csv contiene algun error, por lo que no se puede "jugar" con el
    dt = pd.read_csv("reviews_filmaffinity.csv")

    grafico = Grafico(dt,"film name","review_rate")
    grafico.grafico_barras("Critica Peliculas Españolas")

    #Esta media no tiene mucho sentido, ya que es la columna "film_avg_rate" es el promedio de "review_rate"
    #No obstante esto es orientativo, unicamente para trabajar con un dataset grande
    media = Media(dt,"film_avg_rate","review_rate")
    print ("La media es {}".format(media.calcular_media()))

    #Ocurre lo mismo que con la media en el caso de la desviacion estandar
    desviacion_estandar = Std(dt,"film_avg_rate","review_rate")
    print ("La desviacion estandar es {}".format(desviacion_estandar))


    porcentaje_ = Porcentaje(dt,"film_avg_rate","review_rate")
    for i in range(1,4):
        print ("{}º porcentaje: {}%".format(porcentaje_.porcentaje(i)))
    #Estos porcentajes deberian salir 68% el primero, 95% el segundo y 99.7% el tercero
    #Terriblemente, no podemos comprobarlo debido al csv. Aun asi, confio plenamente en mi teoria
```

---
