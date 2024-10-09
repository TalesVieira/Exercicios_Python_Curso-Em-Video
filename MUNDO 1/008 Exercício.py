# Nome do vídeo: Conversor de Medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Lê um valor em metros e o armazena como um número decimal
medida = float(input('Uma distância em metros: '))

# Converte a medida de metros para centímetros
cm = medida * 100

# Converte a medida de metros para milímetros
mm = medida * 1000

# Exibe as conversões de metros para centímetros e milímetros
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
