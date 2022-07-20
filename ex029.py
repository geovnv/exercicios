v = int(input('A quantos kilomentos você passou no radar hein? '))
c = (v - 80) * 7.00
print('Calculando base de dados.....')
if v > 80:
    print('SE FUDEU! VOCÊ FOI MULTADO, sua multa é de: R${:.2f}'.format(c))
else:
    print('ESSA FOI POR POUCO, NÃO LEVOU MULTA!')
