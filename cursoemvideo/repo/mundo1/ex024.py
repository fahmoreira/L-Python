print('==== Desafio 24 ====')

# Crie um programa que leia o nome de uma cidade diga se 
# ela começa ou não com o nome "SANTO".

#cidade = str(input('Nome da cidade: ')).strip()
cidade = 'Santo Antônio do Rio Abaixo'.strip() # Função strip para eliminar os espaços
print(cidade[:5].upper() == 'SANTO') # Pode ser upper ou lower, porém é só para deixar o stream padrão
