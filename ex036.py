valor = float(input('Qual o valor da casa que pretende comprar? R$ '))
salario = float(input('Qual seu salário mensal? R$'))
tempo = int(input('Em quantos anos pretende quitar o empréstimo? '))
emp = valor / (tempo * 12)
minimo = salario * 30 / 100
print ('Para pagar uma casa no valor de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, tempo, emp))
if emp <= minimo:
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print ('EMPRÉSTIMO NEGADO!')