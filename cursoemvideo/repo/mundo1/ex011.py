print('==== Desafio 11 ====')
#Faça um programa que leia a largura e a altura de uma
#parede em metros. Calcule a sua área e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro
#de tinta pinta uma área de 2m(2).

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area_t = larg * alt
#O oposto de potenciação é raiz, portanto, 
#foi necessário a tranformação de mt² para ter-se mais
#exatidão no resultado. Normalmente o calculo é x**(1/2) para raiz quadrada, 
#x**(1/3) para raiz cúbica e etc#
liter_per_meter = (2**0.5)**2
qtd_tinta = area_t / liter_per_meter
print('A parede possui {:.2f} mt².\nA quantidade de tinta para pintar a parede é {:.2f} lt por mt².'.format(area_t, qtd_tinta))