print('==== Desafio 20 ====')
# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre
# a ordem sorteada.

from random import shuffle

'''seq = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
lista = []
for seqn in seq:
    for aluno in range(len(seq)):
        aluno = str(input('Digite o nome do {} aluno: '.format(seqn)))
        lista.append(aluno)
        break

print(lista)
shuffle(lista)
print('A sequência aleatória é {}'.format(lista))'''

def aleatorio(lista):
    result = []
    for aluno in lista:
        result.append(aluno)
        shuffle(result)
    return result

nomes = ['Alex', 'Fabinho', 'Jhony', 'Olafh']
print(aleatorio(nomes))
