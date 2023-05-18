#Ler o numero de carros vendidos e o valor total das vendas do vendedor 
#Calcular o salario do vendedor, sabendo que o salario_fixo é de 622,00, comissao de 30 reais por carro vendido e *5/100 do valor total das vendas
salario = 622.00
comissão = 30.00
carros_vendidos = float(input('Escreva o número de carros vendidos: '))
vendas_totais = float(input('Escreva o valor total das suas vendas: '))
extra = comissão * carros_vendidos
salario_total = salario + extra + (vendas_totais *5/100)
print('O salario do vendedor neste mês foi de :', salario_total, 'Reais')

