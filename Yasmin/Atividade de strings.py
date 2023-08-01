#Questão 1
#palavra = input('Digite uma palavra: ')
#letra = input('Digite uma letra: ')
#contador = palavra.count(letra)
#if contador >= 1:
#    print(f'Essa palavra possui a letra "{letra}" {contador} vez ou vezes.')
#else:
#    print(f'Essa palavra não possui a letra "{letra}".')

#Questão 2
#frase = input('Digite uma frase: ')
#palavras = frase.split()
#print(f'Essa frase tem {len(palavras)} palavras.')

#Questão 3
s = input('Diga algo: ')
i = int(input('Digite um número: '))
j = int(input('Digite mais um número: '))
quant = len(s)
if i <= quant and j <= quant:
    print('Os números não ultrapassam o tamanho da string.')
    print(s[i:j])
else:
    while i >= quant or j >= quant:
        i = int(input('Digite um número: '))
        j = int(input('Digite mais um número: '))
    print('Os números não ultrapassam o tamanho da string.')
    print(s[i:j])



