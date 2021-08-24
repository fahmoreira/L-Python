# Desenvolva uma lógica que leia o peso e a altura de uma 
# pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

altura = float(input('Digite a altura (m): '))
peso = float(input('Digite o peso (kg): '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('O IMC é {:.2f} kg/m²: Está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25: # 18.5 <= imc < 25 forma que o professor trouxe
    print('O IMC é {:.2f} kg/m²: Está com o peso ideal!'.format(imc))
elif imc >= 25 and imc < 30: # 25 <= imc < 30
    print('O IMC é {:.2f} kg/m²: Está com Sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40: # 30 <= imc < 40
    print('O IMC é {:.2f} kg/m²: Está com OBESIDADE!'.format(imc))
else:
    print('O IMC é {:.2f} kg/m²: Está com OBESIDADE MÓRBIDA!'.format(imc))
