# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
# ou então o empréstimo será negado.
from time import sleep
val_imovel = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o valor do salário? R$'))
anos = int(input('Quanto tempo será o financiamento? '))

print('-='*20)
# Regras do negócio
max_sal = salario - salario * 0.70
mes = anos * 12
prestacao = val_imovel / mes

print('Calculando empréstimo...\n ')
sleep(2)
print('Sendo o financiamento em {} anos a prestação mensal será de R${:.2f}'.format(anos, prestacao))
if prestacao > max_sal:
    print('O empréstimo será negado, refaça o pedido do empréstimo!')
else:
    print('O seu empréstimo foi APROVADO! Parabéns!')
