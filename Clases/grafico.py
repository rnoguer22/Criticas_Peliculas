from media import Media
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