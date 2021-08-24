# Refaça o DESAFIO 035 dos triângulos, acrescentando o 
# recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))

if (b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b):
    if a == b and a == c:
        print('Trata-se de um triângulo EQUILÁTERO!')
    elif a == b or a == c:
        print('Trata-se de um triângulo ISÓSCELES!')
    elif a != b and a != c:
        print('Trata-se de um triângulo ESCALENO!')
else:
    print('Essas medidas não formam um triângulo!')
