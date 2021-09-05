# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = 13
count = 0
for i in range(1, num+1):
    if num % i == 0:
        print(f'[{i}]', end=', ')
        count +=1
    else:
        print(i, end=', ')
print('Fim!')
if count > 2:
    print(f'\nO número {num} foi divisível {count} vezes!')
    print(f'Não é um número PRIMO!')
else:
    print(f'\nO número {num} foi divisível {count} vezes!')
    print(f'É um número PRIMO!')

'''

### Solução do professor

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % 2 == 0:
        print('\033[33m', end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
