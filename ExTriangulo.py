# Programa que recebe três valores númericos reais que representam os comprimentos dos lados de um triângulo, e verifica se 
# os lados condizem com a figura. Caso a condição seja atendida, o programa classifica o triângulo como equilátero, isósceles ou escaleno.

# Definindo váriaveis para atribuir o valor dos lados do triângulo:

lado_a = float(input('Digite o valor do primeiro lado do triângulo: '))
lado_b = float(input('Digite o valor do segundo lado do triângulo: '))
lado_c = float(input('Digite o valor do tereiro lado do triângulo: '))

# Condicional para verificar se os lados condizem com um triângulo e classificar a sua categoria. Caso
# os lados não condizerem com um triângulo, ele printa uma mensagem de erro.

#verificar se condiz com um triângulo:
if (lado_a + lado_b < lado_c) or (lado_a + lado_c < lado_b) or (lado_b + lado_c < lado_a):
    print ('Não condiz com um triângulo.')
#verificar se é equilátero:
elif lado_a == lado_b and lado_a == lado_c:
    print ('O triângulo é equilátero.')
#verificar se é escaleno:
elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    print ('O triângulo é escaleno.')
#verificar se é isósceles:
else:
    print ('O triângulo é isósceles.')