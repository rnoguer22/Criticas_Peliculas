import pandas as pd
from grafico import Grafico

#El csv contiene algun error, por lo que no se puede "jugar" con el
dt = pd.read_csv("reviews_filmaffinity.csv")

grafico = Grafico(dt,"film name","review_rate")
grafico.grafico_barras("Critica Peliculas Españolas")
