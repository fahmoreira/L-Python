# Refaça o Desafio 009, mostrando a tabuada de um número que 
# o usuário escolher, só que agora utilizando um laço for.

#n = int('Digite um número para ver sua tabuada: ')
n = 8
print(f'A TABUADA DE {n} É: ')
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
