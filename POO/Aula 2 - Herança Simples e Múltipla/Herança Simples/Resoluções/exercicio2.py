class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        print(f'Nome: {self.nome}\nSalário: {self.salario}\nDepartamento: {self.departamento}')

gerente1 = Gerente('Silvana', 7045.90, 'Vendas')
gerente1.exibir_dados()
