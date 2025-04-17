class Pessoa:
    # Construtor da classe com atributos (altura, nome, idade) da instância/objeto (pessoa1)
    # def init é chamado automaticamente quando a instância é criada, e serve para inicializar os atributos do objeto 
    def __init__(self, altura, nome, idade):
        self.altura = altura
        self.nome = nome
        self.idade = idade
        self.falando = False
    
    # Métodos 
    def falar(self):
        if self.falando: # if self.falando == True
            print(f'{self.nome} já está falando')
        else:
            self.falando = True
            print(f'{self.nome} começou a falar.')
    
    def parar_falar(self):
        if not self.falando: # if self.falando == False
            print(f'{self.nome} já não está falando.')
        else:
            self.falando = False
            print(f'{self.nome} parou de falar.')

# Instância da classe Pessoa
pessoa1 = Pessoa(1.70, 'Laura', 21)
p2 = Pessoa(1.60, 'Geovanna', 19)

# Acessando e exbindo atributos
print(f'Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Altura: {pessoa1.altura}')
print(f'Nome: {p2.nome}, Idade: {p2.idade}, Altura: {p2.altura}')

print()

# Execução dos métodos
pessoa1.falar()
pessoa1.falar()
#print(f'Status falando: {pessoa1.falando}')
pessoa1.parar_falar()
pessoa1.parar_falar()
#print(f'Status falando: {pessoa1.falando}')