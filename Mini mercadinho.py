#Codigo como se fosse um mini mercadinho de vendas em PYTHON

#chocolate 1.50 ; Refrigerante 2.00 ; Misto Quente 2.00 ; Sorvete 1.50

choco = float(input('Escreva a quantidade de Chocolates que comeu: '))

refri = float(input('Escreva a quantidade de Refrigerantes que tomou: '))

misto = float(input('Escreva a quantidade de Mistos quentes que comeu: '))

sorv = float(input('Escreva a quantidade de Sorvetes que tomou: '))

chocolate = choco * 1.50

refrigerante = refri * 2.00

misto_quente = misto * 2.00

sorvete = sorv * 1.50

compra_total = chocolate + refrigerante + misto_quente + sorvete

print('O valor total da consumação foi de : ', compra_total, 'Reais')