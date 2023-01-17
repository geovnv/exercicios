produto = ' '
cont = pmaior = pmenor = soma = 0

while True:
    print('-' * 20)
    print('LOJAS GEO')
    print('-' * 20)
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$ '))
    cont += 1
    soma += preço
    if preço >= 1000:
        pmaior += 1
    if cont ==1 or preço < pmenor:
        pmenor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/ N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {pmaior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} custando R${pmenor:.2f}')

