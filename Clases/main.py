import pandas as pd
from grafico import Grafico
from media import Media
from std import Std

#El csv contiene algun error, por lo que no se puede "jugar" con el
dt = pd.read_csv("reviews_filmaffinity.csv")

grafico = Grafico(dt,"film name","review_rate")
grafico.grafico_barras("Critica Peliculas Españolas")

#Esta media no tiene mucho sentido, ya que es la columna "film_avg_rate" es el promedio de "review_rate"
#No obstante esto es orientativo, unicamente para trabajar con un dataset grande
media = Media(dt,"film_avg_rate","review_rate")
print ("La media es {}".format(media.calcular_media()))

#Ocurre lo mismo que con la media en el caso de la desviacion estandar
desviacion_estandar = Std(dt, "film_avg_rate","review_rate")
print ("La desviacion estandar es {}".format(desviacion_estandar))

