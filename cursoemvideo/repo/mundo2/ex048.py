# Faça um programa que calcule a soma entre todos os números 
# ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for i in range(0, 501, 3):
    if i % 2 == 0:
        continue
    else:
        soma+=i
        cont+=1 # Para contar os números que serão somados

print(soma, cont)

'''

### CORREÇÃO/MÉTODO DO PROFESSOR

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        #print(i, end='  ')
        soma+=i
        cont+=1

print(f'A soma de todos os {cont} valores solicitados é: {soma}')