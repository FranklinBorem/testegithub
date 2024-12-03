def calculaArea(x, y):
    return x * y
class Retangulo:
    def __init__(self, area, cor="Verde"):
        self.cor = cor
        self.area = area
meuRetangulo = Retangulo(calculaArea(4, 3), "Azul")

print('olá mundo')