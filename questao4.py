class IngressoCinema():
    def __init__(self):
        self.dia = 0
        self.dia_semana = ""
        self.hora = 0
        self.preco = 0
        self.tipo_ingresso = ""

    def calcular_preco_ingresso(self):
        self.dia = int(input("Digite o dia do mês (1-31): "))
        if self.dia < 1 or self.dia > 31:
            print("Erro: dia inválido.")
            return

        self.dia_semana = int(input("Digite o número do dia da semana (1-Domingo, 7-Sábado): "))
        dias = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
        
        if self.dia_semana < 1 or self.dia_semana > 7:
            print("Erro: número do dia inválido.")
            return
        self.dia_semana = dias[self.dia_semana - 1]
        
        self.hora = int(input("Digite a hora da sessão (hh:mm): ").split(":")[0])
        if self.hora > 23:
            print("Erro: hora inválida.")
            return

        self.tipo_ingresso = input("Digite 's' para meia-entrada ou 'n' para entrada normal: ")
        if self.tipo_ingresso == "s":
            self.tipo_ingresso = "meia"
        elif self.tipo_ingresso == "n":
            self.tipo_ingresso = "normal"
        else:
            print("Erro: tipo de ingresso inválido.")
            return

        self.calcular_valor_ingresso()

    def calcular_valor_ingresso(self):
        if self.dia_semana in ["segunda-feira", "terça-feira", "quinta-feira"]:
            self.preco = 16.00
            if 17 <= self.hora < 23:
                self.preco *= 1.5
            if self.tipo_ingresso == "meia":
                self.preco *= 0.5
        elif self.dia_semana in ["sexta-feira", "sábado", "domingo"]:
            self.preco = 20.00
            if 17 <= self.hora < 23:
                self.preco *= 1.5
            if self.tipo_ingresso == "meia":
                self.preco *= 0.5
        elif self.dia_semana == "quarta-feira":
            self.preco = 8.00

        print(f"Preço do ingresso: {self.preco:.2f} R$")

ingresso = IngressoCinema()
ingresso.calcular_preco_ingresso()
