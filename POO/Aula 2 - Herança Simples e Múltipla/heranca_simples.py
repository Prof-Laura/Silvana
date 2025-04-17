
class veiculo():
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        text = "Ligando motor"
        print(text)

    def status(self):
        return f"Cor: {self.cor} - Placa: {self.placa} - Número de Rodas: {self.num_rodas}"
    

# herdo as características do pai sem sobescrever, ou seja, minha classe filha tem exatemente os mesmos atributos que a classe pai
class moto(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    # método para sobescrever, pois quero característica do pai + algo novo/modificar algo
    def __init__(self, carregado, cor, placa, num_rodas):
            super().__init__(cor, placa, num_rodas) # chama o __init__ da classe pai 
            self.carregado = carregado

    # Sem o super
    """def __init__(self, carregado, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

        self.carregado = carregado"""

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")

motocicleta = moto("preta", "abc", 2)

carros = carro("vermelho", "ert", 4)

caminhoes = caminhao(True, "branco", "qwe3", 8)
caminhoes.ligar_motor()
caminhoes.esta_carregado()

print(motocicleta.status())
print(carros.status())
print(caminhoes.status())