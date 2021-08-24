from time import sleep
from random import randint
# -> Sorte do computador
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(''' Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
print('-='*11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else: 
        print('JOGADA INVÁLIDA!')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else: 
        print('JOGADA INVÁLIDA!')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPARTE')
    else: 
        print('JOGADA INVÁLIDA!')
