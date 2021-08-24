# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
jokenpo = ['pedra', 'papel', 'tesoura']
computador = choice(jokenpo)

escolha = input('Pedra, Papel ou Tesoura? ')
if computador == 'pedra' and escolha == 'pedra':
    print('Empatou!')
elif computador == 'pedra' and escolha == 'papel':
    print('Você ganhou!')
elif computador == 'pedra' and escolha == 'tesoura':
    print('O computador ganhou!')
elif computador == 'papel' and escolha == 'papel':
    print('Empatou!')
elif computador == 'papel' and escolha == 'pedra':
    print('O computador ganhou!')
elif computador == 'papel' and escolha == 'tesoura':
    print('Você ganhou!')
elif computador == 'tesoura' and escolha == 'tesoura':
    print('Empatou!')
elif computador == 'tesoura' and escolha == 'papel':
    print('O computador ganhou!')
elif computador == 'tesoura' and escolha == 'pedra':
    print('Você ganhou!')
else: 
    print('Opção inválida')
