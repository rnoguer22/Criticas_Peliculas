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
        lim_inf = self.media - num*self.desviacion
        lim_sup = self.media + num*self.desviacion
        r = []
        s = []
        for i in range (len(self.dataset)):
            if self.dataset[self.col1][len(self.dataset)-i] >= lim_inf and self.dataset[self.col1][5-i] <= lim_sup:
                r.append(self.dataset[self.col1][i])
                s.append(self.dataset[self.col2][i])
            else:
                pass
        r.sort()
        print (r)

        #Hallamos el porcentaje
        print ("El porcentaje es {}%".format(round(sum(s)/self.dataset[self.col2].sum(), 2)))


datos = {
    "Opinion":[5,4,3,2,1,0],
    "Cantidad de Votantes":[42,96,132,124,88,58]
}

#Creamos el dataframe a partir de los datos del enunciado
dt = pd.DataFrame(datos)

por = Porcentaje(dt, "Opinion", "Cantidad de Votantes")
por.porcentaje(1)