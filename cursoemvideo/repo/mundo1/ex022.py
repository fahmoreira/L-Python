print('==== Desafio 22 ====')
# Exercício Python 22: 
# Crie um programa que leia o nome completo de uma pessoa e mostre
# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

#nome = input('Insira o nome da pessoa: ')
nome = 'Fábio Moreira Silva'
print('\n- Nome: ', nome, '\n')
print('Analisando nome...')
print('- Maiúsculo: ', nome.upper())
print('- Minúscula: ', nome.lower())
#print('- Possui', len(nome.replace(' ', '')), 'letras.')
print('- Possui {} letras.'.format(len(nome) - nome.count(' '))) 
#print('- O primeiro nome possui: ', len(nome.split()[0]), 'letras.')
print('- O primeiro nome possui {} letras.'.format(len(nome.split()[0])))

