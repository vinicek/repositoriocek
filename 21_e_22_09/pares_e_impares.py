# Construa um programa onde o usuário digitará sete números e o programa escreverá,
# na tela, quantos deles são pares e quantos são ímpares.
pares = 0
impares = 0
for i in range (0,7):
    numero = float(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print (f'{pares} números são pares e {impares} números são ímpares')