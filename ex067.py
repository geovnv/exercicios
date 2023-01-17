n = 0
while n >= 0:
        n = int(input('Quer ver a tabuada de qual valor? '))
        if n < 0:
            break
        for t in range(0, 11, 1):
            r = n * t
            print(f'{n} * {t} = {r}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
