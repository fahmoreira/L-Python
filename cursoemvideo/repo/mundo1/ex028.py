print('==== Desafio 28 ====')

# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário vence ou perdeu.

print('\nADIVINHE O QUE O COMPUTADOR ESTÁ PENSANDO')
'''
from random import choice
lista = [1,2,3,4,5]
num = int(input('Em que número eu pensei? '))
escolha = (choice(lista))

if escolha == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(escolha, num))
'''



from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 10)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))