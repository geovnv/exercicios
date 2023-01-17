from random import randint
print('-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 10)
v = 0
while True:
    j = int(input('Digite um valor: '))
    comp = randint(0, 11)
    total = j + comp
    t = ' '
    while t not in 'PI':
        t = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {j} e o computador {comp}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if t == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif t == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
