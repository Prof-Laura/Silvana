class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        return f"Novo Saldo: {self.saldo}"
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque realizado! Novo saldo: {self.saldo}"
        else:
            return "Saque não foi efetuado. Saldo insuficiente."
        
    def mostrar_saldo(self):
        return f"Saldo atual: {self.saldo}"
    
conta1 = ContaBancaria("Laura")
valor = int(input("Qual valor você deseja depositar?\n"))
print(conta1.depositar(valor))
valor = int(input("Qual valor você deseja sacar?\n"))
print(conta1.sacar(valor))

# Se preferir pode ter apenas uma leitura para o saque e o teste pode ser feito rodando o código novamente.
valor = int(input("Qual valor você deseja sacar?\n"))
print(conta1.sacar(valor))
print(conta1.mostrar_saldo())