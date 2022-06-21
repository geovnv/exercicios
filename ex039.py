ano = int(input('Digite sua data de nascimento: '))
idade = 2022 - ano
if idade > 18:
    print('Já passou {} ano(s) do seu alistamento militar!'.format(idade - 18))
elif idade < 18:
    print('Fica tranquilo, ainda faltam {} para o seu alistamento militar!'.format(18 - idade))
elif idade == 18:
    print('Esse é o ano do seu alistamento militar.')
