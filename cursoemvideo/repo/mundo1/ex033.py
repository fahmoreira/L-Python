print('==== Desafio 33 ====')

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Insira o 1º número: '))
n2 = float(input('Insira o 2º número: '))
n3 = float(input('Insira o 3º número: '))
#lista = [n1,n2,n3]

# print('A ordem do maior para o menor é: {}'.format(sorted(lista, reverse=True)))
# print('O menor valor é: {}'.format(min(lista)))
# print('O maior valor é: {}'.format(max(lista)))

# Verificando quem é o MENOR
menor = a
if b < a and b < c:
	menor = b
if c < a and c < b:
    menor = c

# Verificando quem é a MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))