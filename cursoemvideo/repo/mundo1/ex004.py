print('==== Desafio 4 ====\n')
#Dissecando uma variável com .format
some_thing = input('Digite algo:: ')
print('O tipo primitivo é ', type(some_thing))
print('Só tem espaços? {}'.format(some_thing.isspace()))
print('É um número? {}'.format(some_thing.isnumeric()))
print('É alphanumérico? {}'.format(some_thing.isalnum()))
print('Está em maiúsculo? {}'.format(some_thing.isupper()))
print('Está em minúsculo? {}'.format(some_thing.islower()))
print('Está capitalizado? {}'.format(some_thing.istitle()))