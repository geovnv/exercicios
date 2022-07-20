a = int(input('Digite um ano: '))
from calendar import isleap
a1 = isleap(a)
if a1 == True:
    print('{} é um ano bissexto.'.format(a))
else:
    print('{} NÃO é um ano bissexto.'.format(a))
