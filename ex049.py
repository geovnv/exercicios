n = int(input('Digite um número: '))
print('Calculando a tabuada de {}...'.format(n))
for t in range(1, 11):
    print('{} x {:2} = {}'.format(n, t, n*t))
    