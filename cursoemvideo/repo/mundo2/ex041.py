# A Confederação Nacional de Natação precisa de um programa que 
# leia o ano de idade de um atleta e mostre sua categoria, de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
ano_atual = date.today().year

data_nasc = int(input('Qual a data de nascimento? '))
print('\n')
idade = ano_atual - data_nasc

if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Categoria para competição: MIRIM')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Categoria para competição: INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Categoria para competição:JÚNIOR')
elif idade > 19 and idade <= 20:
    print(f'O atleta tem {idade} anos.')
    print('Categoria para competição: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.')
    print('Categoria para competição: MASTER')
