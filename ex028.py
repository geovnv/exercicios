# O QUE EU FIZ:
# n = int(input('Digite um número de 0 a 5: '))
# if n == 2:
# print('Parabéns! VOCÊ GANHOU!')
# else:
# print('VOCÊ PERDEU!')

# O CERTO:
from random import randint
computador = randint(0, 5)  # FAZ O COMPUTADOR PENSAR
print('-=-' * 20)
print('Advinhe o número que estou pensando...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #JODAGOR TENTA ADVINHAR
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI: Eu pensei no número {} e não no {}!'.format(computador, jogador))
