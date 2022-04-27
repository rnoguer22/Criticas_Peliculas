from Clases.media import Media
from math import sqrt

class Std(Media):
    #Constructor
    def __init__(self, dataset, col1, col2):
        #Heredamos el constructor de la clase Media
        super().__init__(dataset, col1, col2)

    def calcular_std(self):

        def columna_std():
            columna = []
            media = self.calcular_media(self.dataset, self.col1, self.col2)
            for i in range(len(self.dataset)):
                resultado = self.dataset[self.col2][i] * (self.dataset[self.col1][i] - media)*(self.dataset[self.col1][i] - media)
                columna.append(resultado)
            return columna

        self.dataset["Ni*((Xi-media)^2)"] = columna_std()
        suma_columna = self.dataset["Ni*((Xi-media)^2)"].sum()
        suma_ni = self.dataset[self.col2].sum()
        varianza = suma_columna/suma_ni

        return sqrt(varianza)