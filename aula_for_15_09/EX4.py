# Construa uma página onde o usuário digitará um valor e o programa mostrará, na tela, a tabuada de multiplicação deste número. 

numero = int(input('Digite o valor que deseja multiplicar: '))
tabuada = int(input('Digite até qual posição da tabuada deseja multiplicar: '))
for n in range(1,tabuada+1):
    print (numero*n)
