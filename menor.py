# como achar o menor valor entre dois numeros

# Passo 1 -> Ter 2 números
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

# Passo 2 -> Testar condicional

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 == numero2:
    print(f'{numero1} é igual {numero2}')
else:
    print(f'{numero1} é menor {numero2}')

