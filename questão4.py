class ContaCorrente():
    def __init__(self):
        self.nome_titular = ""
        self.numero_conta = 0
        self.saldo_atual = 0

    def realizar_saque(self):
        valor_saque = int(input("Digite o valor para saque: "))
        if valor_saque <= self.saldo_atual:
            self.saldo_atual -= valor_saque
        else:
            print("Saldo insuficiente para este saque.")

    def realizar_deposito(self):
        valor_deposito = int(input("Digite o valor para depósito: "))
        self.saldo_atual += valor_deposito
        print(f"Depósito realizado! Novo saldo: {self.saldo_atual} R$")

conta = ContaCorrente()
conta.nome_titular = "emy_yas"
conta.numero_conta = 1234567890
conta.saldo_atual = 100.0
conta.realizar_saque()
print(f"Saldo atual: {conta.saldo_atual} R$")
conta.realizar_deposito()
print(f"Saldo atual após depósito: {conta.saldo_atual} R$")
