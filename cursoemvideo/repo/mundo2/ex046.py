# Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artifício, indo de 10 até 0, 
# com uma pausa de 1 segundo entre eles.

# https://unicode.org/emoji/charts/emoji-list.html

from time import sleep
# for i in range (10, -1, -1) CORREÇÃO DO PROFESSOR
for i in range(1,11, 1):
    n = 11
    print(n - i)
    sleep(0.5)
print('\U0001F4A5'*10)
print('FELIZ')
print('\U0001F38A'*10)
print('ANO')
print('\U0001F387'*10)
print('NOVOOOOOOOOO!')
print('\U0001F386'*10)
print('\N{winking face}')
