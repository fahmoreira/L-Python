# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não 
# atingiram a maioridade e quantas já são maiores.
from datetime import datetime
anoatual = datetime.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}º nasceu: '))
    if anoatual - ano >= 18:
        maior+=1
    else:
        menor+=1

print(f'São {maior} os maiores de idade.')
print(f'São {menor} os menores de idade.')
        
    
