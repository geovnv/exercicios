from random import randint
c = randint(0, 10)
print('-=-' * 20)
print('Advinhe o número que estou pensando...')
print('-=-' * 20)
print('Você consegue acertar qual número eu pensei? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == c:
        acertou = True
print('PARABÉNS! Você acertou!')
print(f'Você tentou {palpites} vezes até acertar o número de pensei!')
