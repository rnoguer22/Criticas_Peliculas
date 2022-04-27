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