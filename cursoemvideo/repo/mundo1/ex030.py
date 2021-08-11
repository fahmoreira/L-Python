print('==== Desafio 30 ====')

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número para ver se é PAR ou ÍMPAR: '))

if (num % 2) == 0:
    print('{} é um número PAR!')
else:
    print('{} é um número ÍMPAR!'.format(num))