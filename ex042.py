l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
print('......CALCULANDO......')
if l1 == l2 and l2 == l3:
    print('Esses números formam um triângulo equilátero.')
elif l1 != l2 and l2 != l3 and l1 != l3:
    print('Esses números formam um triângulo escaleno.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Esses números formam um triângulo isósceles.')
