# 1. Cálculo de Lâmpadas: 
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada

potencia=3
largura=float(input('Quanto de largura tem o cômodo?'))
comprimento=float(input('Quanto de comprimento tem o cômodo?'))

lampadas=(largura*comprimento)/potencia
print(f'Seriam necessárias {lampadas} lampadas para iluminar o cômodo.')

# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²

caixa=1.5
largura=float(input('Quanto de largura tem o cômodo?'))
comprimento=float(input('Quanto de comprimento tem o cômodo?'))
altura=float(input('Quanto de comprimento tem o cômodo?'))

resultado=(largura*comprimento*altura)/1.5
print(f'Ira precisar de {resultado} caixas de azulejos')


# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

combustivel=6.15
inicio=float(input('Escreva quantos KM o carro estava no inicio da corrida:'))
final=float(input('Escreva quantos KM o carro estava no final da corrida:'))
gasto=float(input('Escreva quantos litros de combustivel foi gasto:'))
ganhos=float(input('Escreva quanto recebeu no total dos clientes:'))

calculo=(inicio-final)