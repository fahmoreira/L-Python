# Crie um programa que mostre na tela todos os pares que estão no intervalo entre 1 e 50.
'''
def count_even(qtd_vezes):
    for i in range(1, qtd_vezes+1):
        if i % 2 == 0:
            print(i)
        else:
            continue

print(count_even(50), end=' ')
'''
### Correção do exercício + explicações

'''
for n in range(1, 51):
    print('.', end='') 
    # Fazer uso do print desta forma da para enxergar quantas vezes esta acontecendo a iteração
    # Da forma como está feito o algorítmo o processador tem uma carga a mais do que o necessário
    # (Fazer teste tirando o parênteses)
    # Saída: .. 2.. 4 .. 6 .. 8 ..
    if n % 2 == 0:
        print(n, end='  ') # A utilização dos 2 espaços faz com que a impressão seja na horizontal 

'''

### Sabendo que uma das iterações não é importante:

for n in range(2, 51, 2):
    print('.', end='')
    print(n, end='  ')
print('Acabou')

# Saída: # .2  .4  .6  .8  .10  .12
# Fazendo assim metade das repetições ocupando do processador METADE do tempo.
