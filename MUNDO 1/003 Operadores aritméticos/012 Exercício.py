# Nome do vídeo: Calculando Descontos
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# Lê o preço do produto
preço = float(input('Qual é o preço do produto? R$ '))

# Calcula o novo preço com desconto de 5%
novo_preço = preço - (preço * 5 / 100)

# Exibe o resultado
print('O produto que custava R${:.2f}, na promoção com desconto de 5%, vai custar R${:.2f}'.format(preço, novo_preço))
