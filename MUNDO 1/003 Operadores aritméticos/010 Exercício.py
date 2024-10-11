# Nome do vídeo: Conversor de Moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$ 3,27

# Lê o valor em reais que a pessoa tem na carteira
real = float(input('Quanto dinheiro você tem na carteira? R$'))

# Calcula quantos dólares a pessoa pode comprar
dolar = real / 3.27

# Exibe o resultado formatado
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
