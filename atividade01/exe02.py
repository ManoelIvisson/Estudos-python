quant_pessoas = int(input('Digite a quantidade de pessoas da viajem: '))
distancia = float(input('Digite a distancia do trajeto: '))
preco_combustível = float(input('Digite o preço do combustível: '))
media_consumo = float(input('Digite a média de consumo do automóvel: ')) #quantidade de quilometros que consomem 1 litro de combústivel

litros = distancia/media_consumo
gasto = litros * preco_combustível #Valor total da viagem
divisao = gasto/quant_pessoas #valor dividido entre os professores

print(f'O valor que cada professor terá que pagar é R${divisao:.2f}')
