# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# > A média de idade do grupo
# > Qual é o nome do homem mais velho
# > Quantas mulheres têm menos de 70 anos

'''
somaidade = 0
mcount = 0

for i in range(1, 5):
    print(f'---- {i}º PESSOA -----')
    nome = input(f'Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Masculino ou Feminino: ')).lower()

    somaidade+=idade
    if i == 1 and (sexo == 'masculino' or sexo == 'm'):
        n_nome = nome
        n_idade = idade
    elif sexo == 'masculino' or sexo == 'm' and (idade > n_idade):
        n_nome = nome
        n_idade = idade
    elif sexo == 'feminino' or sexo == 'f' and (idade < 20):
        mcount+=1


print(f'A média de idade do grupo é de {somaidade/4:.1f}.')
print(f'O homem mais velho se chama {n_nome} e tem {n_idade}.')
print(f'Ao todo são {mcount} mulheres com menos de 20 anos.')


'''

### SOLUÇÃO DO PROFESSOR
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'---- {p}º PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade 
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
        
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade  / 4

print(f'A média de idade do grupo é de {mediaidade} anos')
pritn(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
