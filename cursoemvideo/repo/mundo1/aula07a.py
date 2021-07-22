n1 = int(input('Digito um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
mult = n1 * n2
div = n1 / n2
div_in = n1 // n2
exp = n1 ** n2
print('A soma é {}, \n o produto é {}, a divisão é {:.3f}'.format(s, mult, div), end=' ')
print('Divisão inteira {}, \n e a potência {}'.format(div_in, exp))
