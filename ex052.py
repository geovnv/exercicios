n = int(input('Digite um número: '))
print("Calculando se esse número é um número primo...")
for c in range (1, n + 1):
    if n % n == 0 and n % 1 == 0:
        print('{} é um número primo.'.format(n))
    else:
        print("{} NÃO é um número primo.".format(n))