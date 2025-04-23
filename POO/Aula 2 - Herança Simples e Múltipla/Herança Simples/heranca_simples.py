### Herança Simples ###

# Classe pai/base
class Veiculo():
    def __init__(self, placa, cor, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    # Métodos
    def ligar_motor(self):
        print("Ligando o motor...")

    def status(self):
        return f"Cor: {self.cor} - Placa: {self.placa} - Numero de Rodas: {self.num_rodas}"
    
# Começo a herança simples
# Herdo as características do pai (Veiculo) sem sobrescrever, ou seja, minha classe filha (moto) tem exatamente os mesmos atributos que a classe pai
class Moto(Veiculo):
    pass

class Caminhao(Veiculo):
    # Método para sobrescrever a classe pai (Veiculo), pois eu quero característica do pai + algo novo ou + modificar algo
    def __init__(self, placa, cor, num_rodas, carregado):
        super().__init__(placa, cor, num_rodas) # chamando o __init__ (construtor) da classe pai
        self.carregado = carregado

    # Sem o super
    """def __init__(self, placa, cor, num_rodas, carregado):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas"""
        
    # Método da classe caminhão
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")
        """if self.carregado == True:
            print("Sim estou carregado")
        else:
            print("Não estou carregado")"""
        
## Instanciar novos objetos ##
# Intanciando moto / classe sem sobrescrever
print("-"*5 + "Usando a classe moto" + "-"*5)
motocicleta = Moto("ABC-123", "Preta", 2)
print(motocicleta.status())
motocicleta.ligar_motor()
print()

# Instanciando caminhao / classe sobrescrevendo
print("-"*5 + "Usando a classe caminhao" + "-"*5)
caminhoes = Caminhao("ABC-4321", "Branco", 8, True)
caminhoes.ligar_motor()
print(caminhoes.status())
caminhoes.esta_carregado()
