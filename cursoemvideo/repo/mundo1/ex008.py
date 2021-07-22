print('==== Desafio 8 ====')
#Escreva um programa que leia um valor em metros e o
#exiba convertido em centímetros e milímetros.
mt = float(input('Digite a metragem:: '))
to_dm = mt * 10 #decímetros
to_cem = mt * 100 #centímetros
to_mm = mt * 1000 #melímetros
to_dam = mt / 10 #Decâmetros
to_hm = mt / 100 #Hequitômetros
to_km = mt / 1000 #Kilometros

print('centimeters is {}cm\nMilimeters is {}mm\nDecimeters is {}dm. '.format(to_cem, to_mm, to_dm))
print('Decâmetros is {}dam\nHectômetros is {}hm\nKilômetros is {}km'.format(to_dam , to_hm, to_km ))
