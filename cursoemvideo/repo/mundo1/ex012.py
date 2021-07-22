print('==== Desafio 12 ====')
#Faça um algoritmo que leia o preço de um produto e
#mostre seu novo preço com 5% de desconto.
prd_value = float(input('Qual o valor do produto? R$'))
desc = prd_value - (prd_value * 0.05)
print('O produto com desconto de 5% será R${:.2f}'.format(desc))