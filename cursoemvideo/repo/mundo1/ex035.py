print('==== Desafio 35 ====')


#Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)


a = float(input('Insira o 1º comprimento: '))
b = float(input('Insira o 2º comprimento: '))
c = float(input('Insira o 3º comprimento: '))

if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    print('Os comprimentos PODEM formar um triângulo')
else:
    print('Os comprimeiros NÃO PODEM formar um triângulo')
