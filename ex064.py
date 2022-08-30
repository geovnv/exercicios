cont = 0
n = 0
s = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += n
    if n == 999:
        s = cont - n
print(f'A soma entre os números digitados é {s}')

