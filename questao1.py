import math

class Circunferencia():
    def __init__(self):
        self.raio = 0

    def calcular_area(self):
        self.area = math.pi * (self.raio ** 2)
        print(f"Área do círculo: {self.area:.2f} unidades quadradas")

    def calcular_circunferencia(self):
        self.circunferencia = 2 * math.pi * self.raio
        print(f"Circunferência do círculo: {self.circunferencia:.2f} unidades")

circulo = Circunferencia()
circulo.raio = int(input("Digite o raio do círculo: "))
circulo.calcular_area()
circulo.calcular_circunferencia()
