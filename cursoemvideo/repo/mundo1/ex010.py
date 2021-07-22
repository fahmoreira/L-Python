print('==== Desafio 10 ====')
#Crie um programa que leia quanto dinheiro uma
#pessoa tem na carteira e mostre quantos dólares ela
#pode comprar.
#Considere US$ = R$3.27

real = float(input('Quanto dinheiro você tem? R$ '))
dol = 3.27
qtd = real / dol
print('É possível comprar US$ {:.2f}'.format(qtd))