print('==== Desafio 25 ====')

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o nome: ')).upper()
#nome = 'Fábio Moreira Silva'.upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))