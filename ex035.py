l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
print('......CALCULANDO......')
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Esses números formam um triângulo.')
else:
    print('Esses números NÃO formam um triângulo.')
