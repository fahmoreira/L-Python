# Faça um programa que leia o peso de cinco pessoas. No final, 
# mostre qual foi o maior e o menor peso lidos.
'''
lista = []
for i in range(1, 6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    lista.append(peso)

print(f'O MAIOR peso foi: {sorted(lista, reverse=True)[0]}')
print(f'O MENOR peso foi: {sorted(lista, reverse=True)[-1]}')

'''
### SOLUÇÃO DO PROFESSOR

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')
