# Programa onde o usúario informa três números e o programa exibe o maior entre eles

# Criando variáveis para o usuário declarar o valor dos números

n1 = (input('Digite o primeiro número: '))
n2 = (input('Digite o segundo número: '))
n3 = (input('Digite o terceiro número: '))

# Estrutura condicional para verificarmos qual é o maior número entre os três informados pelo usúario
if n1 > n2 and n1 > n3:
    print ('O maior número é o primeiro.')

elif n2 > n3 and n2 > n3:
    print ('O maior número é o segundo.')

elif n3 > n1 and n3 > n2:
    print ('O maior número é o terceiro.')

else:
    print ('Não há maior, os números são iguais.')
