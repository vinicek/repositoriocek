# Construa um programa onde o usuário digitará cinco números e o programa deverá colocar esses números dentro do vetor em ordem crescente.
numeros = []
for i in range (0,5):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

numeros.sort()
print (numeros)