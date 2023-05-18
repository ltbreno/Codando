#Quantidade de KM/L ; Tempo gasto na viagem em minutos ; Velocidade media durante a viagem em KM/H
#Autonomia total da viagem
autonomia = float(input('Digite a autonomia do veiculo: '))
tempo = float(input('Digite o tempo gasto na viagem em minutos: '))
velo_media = float(input('Digite a velocidade media durante a viagem: '))
distancia = velo_media * tempo / 60
autonomia_total = distancia / autonomia
print('O gasto total de combustivel na viagem toda foi de ', autonomia_total, 'litros')