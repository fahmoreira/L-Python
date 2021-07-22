print('==== Desafio 18 ====')
#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo.
import math
#O primeiro momento não foi feito a conversão em radianos, conforme manual: https://docs.python.org/3/library/math.html
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
#print(f"O seno de {ang} é {sin(ang)}.\nO cosseno de {ang} é {cos(ang)}.\nA tangente de {ang} é {tan(ang)}")
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(ang, cosseno))
tangete = math.tan(math.radians(ang))
print('O ângulo de {} tem TANGETE de {:.2f}'.format(ang, tangete))