class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}')

    def cozinhar(self, receita: str):
        print(f'Estou cozinhando um(a) {receita}')

    def andar(self, distancia: float):
        print(f'Vou andar {distancia} metros')

class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, altura: float, cargo: str):
        super().__init__(nome, idade, altura)
        self.cargo = cargo