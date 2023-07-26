from atividade01.pessoa import Pessoa, Funcionario

linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))

for linha in range(1, linhas + 1):
    for coluna in range(1, colunas + 1):
        print(f'{linha}{coluna} ', end='')
    print('')

pessoa = Pessoa(nome='João', idade=20, altura=1.7)

pessoa.dizer_ola()
pessoa.cozinhar("Arroz")

funcionario = Funcionario(nome="Rafael", idade=45, altura=1.8, cargo="Vigilante")

funcionario.dizer_ola()