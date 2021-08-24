# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year

data_nasc =  int(input('Ano de nascimento? '))
serv_militar = ano_atual - data_nasc

print(f'Quem nasceu em {data_nasc} tem {serv_militar} anos em {ano_atual}.')

if serv_militar > 18:
    saldo = serv_militar - 18
    print(f'Já deveria ter se alistado há {saldo} anos.')
    ano = ano_atual - saldo # Ajuste feito como a correção do professor
    print(f'Seu alistamento foi em {ano}.') # Ajuste feito como a correção do professor
elif serv_militar < 18:
    saldo = 18 - serv_militar
    print(f'Ainda não é tempo de alistamento, falta {saldo} anos.')
    ano = ano_atual + saldo # Ajuste feito como a correção do professor
    print(f'Se alistamento será em {ano}.') # Ajuste feito como a correção do professor
elif serv_militar == 18:
    print('É hora de se alistar!')
