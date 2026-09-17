#Desenvolva um programa para registrar as vendas de uma loja ao longo do dia. 
# O programa deve processar múltiplos clientes até que o 
# operador digite 0 no total de compras para encerrar o expediente.

valor_produto = float(input('Insira o valor do produto: '))
valor_total = float()

while valor_produto != 0: 

    while valor_produto != -1:
        valor_total += valor_produto
        valor_produto = float(input('Insira o valor do produto: '))
    print (valor_total)

    if valor_total >= 200:
        valor_descontado = valor_total * 0.9
        print (f'O valor total com desconto é {valor_descontado}')

    elif valor_total >= 100:
        valor_descontado = valor_total * 0.95
        print (f'O valor total com desconto é {valor_descontado}')

    else:
        print(f'O valor total da compra não se enquadra para receber desconto')

    parcelas = int(input('Digite a quantidade de parcelas que deseja, em até 6 vezes: '))

    if parcelas <= 6:
        valor_parcela = valor_total/parcelas
        mes = int()
        for mes in range(0,parcelas):
            mes += 1
            print (f'No mês {mes} o valor da parcela será ({valor_parcela})')





