print('==== Desafio 27 ====')

# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

#nome = str(input('Digite o nome completo: '))
nome = 'Fábio Moreira Silva'.strip()
print('O primeiro nome é: {}'.format(nome.split()[0]))
print('O último nome é: {}'.format(nome.split()[-1]))