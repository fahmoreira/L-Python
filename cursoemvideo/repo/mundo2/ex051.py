# Desenvolva um programa que leia o primeiro termo e a 
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# Pesquisar sobre progressão aritmética.

# Fontes: https://www.educamaisbrasil.com.br/enem/matematica/progressao-aritmetica
# https://www.youtube.com/watch?v=FWzAnfPHiA4

print('='*20)
print('10 TERMOS DE UMA P.A')
print('='*20)

a1 = 25 # primeiro termo
r = 5 # razão
an = a1 + (10-1)*r
#a1 = int(input('Primeiro termo: '))
#r = int(input('Razão'))
'''
# Minha solução
# Como o enunciado solicita que mostre o 10º a solução também é plausível, porém,
# não é flexível  
for i in range(1, 11):
    print(a1, end='  ')
    a1 += r
'''
# Solução do professor
# Aqui ele explica sobre a fórmula para achar o 10 termo
for i in range(a1, an+1, r): # range(start, stop, step) no campo stop o professor colocou an+Razão(r)
    print(i, end='  ')


if r > 0:
    print('\nTrata-se de uma P.A crescente.\n')
elif r < 0:
    print('\nTrata-se de uma P.A descrecente.\n')
else:
    print('\nTrata-se de uma P.A constante.\n')
    

