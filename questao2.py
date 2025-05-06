class Jornada():
    def __init__(self):
        self.distancia = 0
        self.duracao = 0

    def calcular_velocidade_media(self):
        horas_minutos = self.duracao.split(":")
        horas_em_decimal = int(horas_minutos[0]) + int(horas_minutos[1]) / 60
        velocidade = self.distancia / horas_em_decimal
        print(f"Velocidade média: {velocidade:.2f} km/h")

viagem = Jornada()
viagem.distancia = int(input("Digite a distância percorrida (km): "))
viagem.duracao = input("Digite o tempo de viagem (hh:mm): ")
viagem.calcular_velocidade_media()
