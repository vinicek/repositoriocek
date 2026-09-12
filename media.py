# Programa que o usúario digitará duas notas e o programa irá calcular a média e informar se o aluno foi aprovado ou reprovado.

# Criando as variáveis para declarar os valores das notas
 
n1 = float(input('Digite a primeira nota: ' ))
n2 = float(input('Digite a segunda nota: ' ))

# Definindo outra variável para calcular o valor da média

media_do_aluno = (n1 + n2)/2 

# Estrutura condicional para verificarmos a situação final do aluno

if media_do_aluno >= 6:
    print ('Aluno Aprovado')

else: 
    print ('Aluno Reprovado')

    