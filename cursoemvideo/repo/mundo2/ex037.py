#Escreva um programa que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão:

# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

# Fonte: https://docs.python.org/3/library/functions.html

print('-='*20)
print('Conversor de Sistema de Numeração')
print('-='*20)


num = int(input('Digite um número: '))
print('\nEscolha a opção para converter!')
print('-='*10)
print('''1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL''')
print('-='*10)

opc = input('Escolha a opção: ')
if (opc > '3') or (opc < '1'):
    print('Opção inválida, reiniciei o programa!')
elif opc == '1':
    print('O {} em BINÁRIO é {}'.format(num, f'{num:b}'))
elif opc == '2':
    print('O {} em OCTAL é {}'.format(num, f'{num:o}'))
elif opc == '3':
    print('O {} em HEXADECIMAL é {}'.format(num, f'{num:x}'))
else:
    print('Opção inválida!')
