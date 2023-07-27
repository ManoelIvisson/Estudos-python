def menu():
    print('Bem vindo ao Analisador de Funções! Escolha qual tipo de função deseja analisar: ')
    print('1 - Função Afim')
    print('2 - Função Quadrática')
    opcao = int(input('Opção: '))

    if opcao == 1:
        analise_afim()
    else:
        analise_quadratica()


def analise_afim():
    valor_a = float(input('Digite o valor do a da função: '))
    valor_b = float(input('Digite o valor do b da função: '))

    print(f'Função f(x) = {valor_a}x + {valor_b}')

    # Análise do zero da função
    if valor_a != 0:
        zerodafuncao = -(valor_b / valor_a)
        print(f'O zero da função é igual a {zerodafuncao}')

        # Análise do gráfico da função, se é crescente ou decrescente
        if valor_a > 0:
            print('O gráfico da função é crescente')
            print(f'Para os valores de X maiores do que {zerodafuncao} a função é positiva')
            print(f'Para os valores de X menores do que {zerodafuncao} a função é negativa')
        else:
            print('O gráfico da função é decrescente')
            print(f'Para os valores de X maiores do que {zerodafuncao} a função é negativa')
            print(f'Para os valores de X menores do que {zerodafuncao} a função é positiva')
    else:
        print('O gráfico da função é constante')
        if valor_b == 0:
            print('Todos os valores de X são o zero da função')
        else:
            print('A função não possui o zero da função!')


def analise_quadratica():
    valor_a = float(input('Digite o valor do a da função: '))
    valor_b = float(input('Digite o valor do b da função: '))
    valor_c = float(input('Digite o valor do c da função: '))


    print(f'Função f(x) = {valor_a}x² + {valor_b}x + {valor_c}')
    


menu()

