salario = 1000
# desconto inicial
desconto = 0
print ("desconto inicial R$" + str(desconto))

# desconto da passagem 
passagem = 6/100 * salario
desconto = passagem
print ("desconto de passagem é de: R$" + str(desconto))

# desconto do vr
vr = 2/100 * salario
desconto = desconto + vr
print ("desconto de VR é de: R$" + str(desconto))

# desconto plano de saude
plano = 10/100 * salario
desconto = desconto + plano
print ("desconto de plano de saúde é de: R$" + str(plano))
print ("Seu desconto total é de: R$" + str(desconto))


# salario liquido
liquido = salario - desconto
print  ("Seu salário líquido é : R$" + str(liquido))