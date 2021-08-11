print('==== Desafio 34 ====')

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

s_atual = float(input('Qual é o salário do funcinoário? R$'))

novo_salario = s_atual + (s_atual * 0.10) if s_atual > 1250 else s_atual + (s_atual * 0.15)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(s_atual, novo_salario))

