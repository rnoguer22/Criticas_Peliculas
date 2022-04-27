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

        #Redondeamos la media a la centesimas
        return suma_xini/suma_ni