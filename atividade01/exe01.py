salario = float(input('Digite seu salário: '))
percentual = float(input('Digite o percentual do aumento do salário: '))
aumento = salario * (percentual/100) #pega o valor do aumento do salario pela porcentagem
salario_novo = salario + aumento

print(f'Seu salário antigo era R${salario:.2f}') #Esse .2f é para limitar/acrescentar duas casas decimais, representação do dinheiro.
print(f'O valor do acrescentado ao salário é R${aumento:.2f}')
print(f'O seu novo salário é R${salario_novo:.2f}')
