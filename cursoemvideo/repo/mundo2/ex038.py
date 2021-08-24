# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

if a > b:
    print('O primeiro número é maior.')
elif a < b:
    print('O segundo número é menor.')
else:
    print('Não existe número maior, os dois são iguais.')
