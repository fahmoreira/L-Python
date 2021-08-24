# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro / cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros


preco = float(input('Preço do produto: R$ '))

print('-='*20)
print('''Opções de pagamento:\n
[ 1 ] - À vista dinheiro / cheque:
[ 2 ] - À vista no cartão: 
[ 3 ] - 2x no cartão:
[ 4 ] - 3x ou mais no cartão: \n''')
opc = input('Digite a opção de pagamento: ')
print('-='*20)

desc1 = preco - preco * 0.10
desc2 = preco - preco * 0.05

if opc != '1' and opc != '2' and opc != '3' and opc != '4':
    print('Opção Inválida! Reinicie o programa.')
elif opc == '1':
    print('Economia de {:.2f}, o produto custará R${:.2f}!'.format((preco - preco * 0.90),desc1))
elif opc == '2':
    print('Economia de {:.2f}, o produto custará R${:.2f}!'.format((preco - preco * 0.95),desc2))
elif opc == '3':
    print('Sem juros! Primeira parcela de R${:.2f}'.format(preco/2))
elif opc == '4':
    qtd_parc = int(input('Quantas parcelas? '))
    total = (preco * 0.20) + preco
    parcelas = total / qtd_parc
    juros = total - preco
    print(f'Juros de R${juros:.2f} que será diluido nas parcelas.')
    print(f'O produto de R${preco:.2f}, custará R${total:.2f} e {qtd_parc}x de R${parcelas:.2f}')
else:
    print('Opção errada!')
