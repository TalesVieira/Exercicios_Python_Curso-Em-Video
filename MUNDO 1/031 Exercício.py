# Nome do vídeo: Custo da viagem
# Este programa calcula o preço de uma passagem de viagem com base na distância percorrida.

# Lê a distância da viagem em quilômetros, inserida pelo usuário
distância = float(input('Qual é a distância de sua viagem? '))

# Exibe a distância da viagem para o usuário
print('Você está prestes a começar uma viagem de {}km'.format(distância))

# Calcula o preço da passagem com base na distância:
# - R$0,50 por km para viagens até 200km (inclusive)
# - R$0,45 por km para viagens com mais de 200km
preço = distância * 0.50 if distância <= 200 else distância * 0.45

# Exibe o preço final da passagem
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
