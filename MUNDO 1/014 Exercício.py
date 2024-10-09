# Nome do vídeo: Conversor de Temperaturas
# Escreva um programa que converta uma temperatura digitada em Celsius e converta para Fahrenheit.

# Lê a temperatura em Celsius
c = float(input('Informe a temperatura em °C: '))

# Converte Celsius para Fahrenheit
f = (9 * c / 5) + 32

# Exibe o resultado
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(c, f))
