resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / n
print(f'Você digitou {quant} números e a média dos números digitados foi {media}')
print(f'O maior número digitado foi o {maior}')
print(f'O menor número digitado foi o {menor}')
