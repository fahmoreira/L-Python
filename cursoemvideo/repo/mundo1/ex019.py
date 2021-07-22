print('==== Desafio 19 ====')
# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
lista = []
for aluno in range(0, 4):
    aluno = str(input('Digite o nome de 4 alunos: '))
    lista.append(aluno)
# lista = ['Alex', 'Fabinho', 'Jhony', 'Olafh']
print('O aluno escolhido foi: {}'.format(choice(lista)))
