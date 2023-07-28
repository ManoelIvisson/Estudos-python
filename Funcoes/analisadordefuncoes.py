def menu():
    print('Bem vindo ao Analisador de Funções! Escolha qual tipo de função deseja analisar: ')
    print('1 - Função Afim')
    print('2 - Função Quadrática')
    opcao = int(input('Opção: '))

    if opcao == 1:
        analise_afim()
    else:
        analise_quadratica()


def analise_afim(valor_a = 0, valor_b = 0):
    if valor_a == 0 and valor_b == 0:
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
            print(f'Para os valores de X maiores do que {zerodafuncao:.2f} a função é positiva')
            print(f'Para os valores de X menores do que {zerodafuncao:.2f} a função é negativa')
        else:
            print('O gráfico da função é decrescente')
            print(f'Para os valores de X maiores do que {zerodafuncao:.2f} a função é negativa')
            print(f'Para os valores de X menores do que {zerodafuncao:.2f} a função é positiva')
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
    delta = (valor_b ** 2) - (4 * valor_a * valor_c)
    raizes = []

    if valor_a == 0:
        print('Quando o valor do coeficiente a é igual a zero a Função Quadrática passa a ser uma Função Afim')
        analise_afim(valor_b, valor_c)
    else:
        vertice_x = -valor_b / (2 * valor_a)
        vertice_y = -delta / (4 * valor_a)

        print(f'Função f(x) = {valor_a}x² + {valor_b}x + {valor_c}')
        print(f'O valor do delta encontrado foi {delta}')

        if delta >= 0:
            # Adiciona uma das raízes a lista raizes pela fórmula de Baskhara
            raizes.append((-valor_b + (delta ** 0.5)) / (2 * valor_a))

            # Adiciona a outra raíz a lista raizes pela fórmula de Baskhara
            raizes.append((-valor_b - (delta ** 0.5)) / (2 * valor_a))

            if delta == 0:
                print(f'Só existe uma raiz real, ela é {raizes[0]}')
            else:
                print(f'As raízes encontradas foram: x1 = {raizes[0]:.2f} e x2 = {raizes[1]:.2f}')

        else:
            print("Essa função não possui raíz real")

        # Verifica a concavidade da parábola
        if valor_a > 0:
            print('A concavidade da parábola é para cima')
            print(f'O valor mínimo da parábola em x e y, respctivamente é: ({vertice_x},{vertice_y})')
            print(f'Para os valores de x menores que {vertice_x} a parábola é decrescente')
            print(f'Para os valores de x maiores que {vertice_x} a parábola é crescente')
        else:
            print('A concavidade da parábola é para baixo')
            print(f'O valor máximo da parábola em x e y, respctivamente é: ({vertice_x},{vertice_y})')
            print(f'Para os valores de x menores que {vertice_x} a parábola é crescente')
            print(f'Para os valores de x maiores que {vertice_x} a parábola é decrescente')


menu()

