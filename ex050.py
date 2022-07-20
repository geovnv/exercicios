soma = 0
cont = 0
for par in range(1, 7):
    num = int(input('Digite o {} valor: '.format(par)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES, e a soma deles será de: {}'.format(cont, soma))
