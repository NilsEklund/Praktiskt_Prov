# Author: Nils Eklund
# Date: 2024-09-25

values = input('Vilka tabeller vill du beräkna? ')

values = values.split(' ')

amount_of_tables = len(values)

try:
    for counter in range(0,amount_of_tables):
        for multiple in range(1,11):
            product = int(values[counter]) * multiple
            print(f'{values[counter]} * {multiple} = {product}')

        print('')
except:
    exit()