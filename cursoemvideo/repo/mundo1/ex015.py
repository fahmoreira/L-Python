print('==== Desafio 15 ====')
#Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado e a quantidade de dias pelas
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0,15 por Km rodado.

days = float(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
paidout = (days * 60) + (km * 0.15)
print('Total a pagar é de R${:.2f}'.format(paidout))
