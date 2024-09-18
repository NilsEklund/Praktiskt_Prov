#Author: Nils Eklund
#Date: 2024-09-18

print('Ei23 - genrep praktiskt prov ht24')
resistor_value = input('Enter the value of each resistor: ')

resistor_value = resistor_value.split(' ')

antal_resistorer = len(resistor_value)
serieresistans = 0
parallellresistans = 0
try:
    for i in range(0,antal_resistorer):
        serieresistans += int(resistor_value[i])
        parallellresistans += (1 / int(resistor_value[i]))
    parallellresistans = 1 / parallellresistans
except:
    serieresistans = 0
    parallellresistans = 0

print(f'Serieresistans: {serieresistans} ohm')
print(f'Parallellresistans: {parallellresistans} ohm')