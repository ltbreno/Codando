#Percentual do distribuidor = 28% do custo de fabrica e os impostos = 45% do custo de fabrica
custo_fabrica =  float(input('Escreva o valor gasto para o carro ser produzido na fabrica: '))
distribuidor = custo_fabrica * 28/100
impostos = custo_fabrica * 45/100
custo_final = custo_fabrica + distribuidor + impostos
print('O custo do carro para o consumidor final é de : ',custo_final, 'Reais')