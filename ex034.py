si = float(input('Digite o salário atual do funcionário: '))
print('.......Calculando o sálario com aumento.......')
s1 = si * 0.1 #VALOR REFERENTE AO AUMENTO DE 10%
s1f = si + s1 #SALÁRIO COM O AUMENTO
s2 = si * 0.15 #VALOR REFERENTE AO AUMENTO DE 15%
s2f = si + s2 #SALÁRIO COM O AUMENTO
if si <= 1250:
    print('O sálario de R${} com o aumento de 15% será de: R${:.2f}'.format(si, s2f))
else:
    print('O sálario de R${} com o aumento de 10% será de: R${:.2f}'.format(si, s1f))
