sexo = str(input('Digite M se o seu sexo for maculino ou F se o seu sexo for feminino: ').upper())
while sexo not in 'MmFf':
    sexo = str(input('Não entendi, digite novamente seu sexo: ').upper())
if sexo == 'F':
    print('Você é do sexo Feminino.')
else:
     print('Você é do sexo Masculino.')
print('FIM')