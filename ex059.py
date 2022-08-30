n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input(' >>>> Qual a opção desejada? '))
    if opção == 1:
        soma = n1 + n2
        print(f' A soma entre {n1} e {n2} é igual a {soma}')
    elif opção == 2:
        mult = n1 * n2
        print(f' A multiplicação de {n1} e {n2} é igual a {mult}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior número é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida - Tente novamente.')
    print('=-=' * 10)
print('Fim do programa!')