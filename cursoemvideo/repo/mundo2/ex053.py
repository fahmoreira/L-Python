# Crie um programa que leia uma frase qualquer e diga 
# se ela é um palindromo, desconsidenrando os espaços.

# Ex: Após a Sopa / A sacada da casa / a torre da derrota 
# / o lobo ama o bolo / anotaram a data da maratona

'''
#string = str(input('Digite uma palavra ou frase: ')).replace(' ', '')
string = '  o lobo ama o bolo  '.replace(' ', '')
compare = string[::-1]

def palindromo(texto): 
    for i in range(len(texto)):
        if texto[i] == compare[i]:
            result = 'PALÍNDROMO'
            continue
        else:
            result = 'NÃO É PALÍNDROMO'
            break
    return result
          
print(palindromo(string))

'''

### SOLUÇÃO DO PROFESSOR

#string = str(input('Digite uma palavra ou frase: ')).replace(' ', '')
string = 'curso em vídeo python'.strip().upper()
palavras = string.split()
junto = ''.join(palavras)
print(junto)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
