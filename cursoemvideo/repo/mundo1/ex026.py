print('==== Desafio 26 ====')

# Faça um programa que leia uma frase pelo teclado e 
# # mostre quantas vezes aparece a letra "A", em que posição ela 
# aparece a primeira vez e em que posição ela aparece a última vez.

#frase = str(input('Digite uma frase: ')).strip()
frase = '    Amanda ama pedro    '.lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição: {}'.format(frase.rfind('a')+1))

#print(len(frase))
#print(len(frase.replace(' ', '')))
