print('==== Desafio 17 ====')
#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo retângulo. Calcule e mostre
#o comprimento da hipotenusa.
#import math
from math import hypot
c_opo = float(input('Cumprimento do cateto oposto: '))
c_adj = float(input('Cumprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2) -> Maneira matemática de fazer a conta
hi = hypot(c_opo, c_adj)
print('A hipotenusa vai medir {:.2f}'.format(hi))
