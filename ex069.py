maioridade = 0
homens = 0
mulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo {M/F} ')).strip().upper()[0]
    if idade < 20 and sexo in 'Ff':
        mulher += 1
    if sexo in 'Mm':
        homens += 1
    if idade >= 18:
        maioridade += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/ N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{maioridade} pessoas possuem mais de 18 anos!')
print(f'{homens} homens foram cadastrados!')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')

