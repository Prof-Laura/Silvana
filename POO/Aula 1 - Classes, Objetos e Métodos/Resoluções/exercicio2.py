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
print(conta1.depositar(200))
print(conta1.sacar(100))
print(conta1.sacar(200))
print(conta1.mostrar_saldo())