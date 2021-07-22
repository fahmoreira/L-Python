print('==== Desafio 13 ====')
#Faça um algoritmo que leia um salário de um funcionário
# e mostre seu novo salário com 15% de aumento.
sm = float(input('Salário atual é R$'))
sm_plus = sm + (sm * 0.15)
print('Com 15% de aumento no salário, será recebido R${:.2f} '.format(sm_plus))