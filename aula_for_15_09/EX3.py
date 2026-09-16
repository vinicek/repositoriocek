numero = int(input('Digite um número: '))
if numero % 2 == 0:
    for i in range(numero, -1, -1):
        print(i)

else:
    print(f'o número {numero} é ímpar.')
