print('==== Desafio 32 ====')

# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = float(input('Insira o ano para checar se é Bissexto: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print("O ano {} Bissexto".format(ano))
else:
    print("O ano {} não é Bissexto!".format(ano))