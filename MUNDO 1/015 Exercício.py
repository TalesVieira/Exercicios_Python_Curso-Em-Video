# Nome do vídeo: Aluguel de carros
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

# Lê a quantidade de dias alugados
dias = int(input('Quantos dias alugados? '))

# Lê a quantidade de KM percorridos
km = float(input('Quantos KM rodados? '))

# Calcula o total a pagar
pago = (dias * 60) + (km * 0.15)

# Exibe o total a pagar formatado com duas casas decimais
print('O total a pagar é de R${:.2f}'.format(pago))
