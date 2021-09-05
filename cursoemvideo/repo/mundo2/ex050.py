# Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for i in range(6):
    num = float(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        soma += num
        cont +=1

print(f'Você informou {cont} número PARES e a soma foi {soma:.1f}')
