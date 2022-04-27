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