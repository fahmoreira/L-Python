print('==== Desafio 29 ====')

# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade >= 81:
    multa = velocidade - 80
    print('Você ultrapassou a velocidade permitida de 80Km/h e será multado em R${:.2f}'.format(multa*7))
else:
    print('Tudo tranquilo! O uso do cinto é obrigatório')