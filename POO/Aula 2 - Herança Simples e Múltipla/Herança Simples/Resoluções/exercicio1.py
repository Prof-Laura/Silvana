class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def falar(self):
        print('O animal está falando')

class Cachorro(Animal):
    pass

cachorrinho = Cachorro('Oliver', 'Canis lupus')
cachorrinho.falar()
print(cachorrinho.nome + ' ' + cachorrinho.especie)
