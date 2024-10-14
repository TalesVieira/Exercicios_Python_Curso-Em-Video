# Nome do vídeo: Aprovando empréstimo
# Este programa calcula se um empréstimo bancário para a compra de uma casa pode ser aprovado.
# A aprovação depende de a prestação mensal não exceder 30% do salário do comprador.

# Entrada de dados: Solicita o valor da casa, o salário do comprador e o prazo de pagamento em anos
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

# Calcula a prestação mensal dividindo o valor da casa pelo número de meses de financiamento
prestacao = casa / (anos * 12)

# Calcula o valor máximo da prestação (30% do salário do comprador)
minimo = salário * 30 / 100

# Exibe o valor da prestação mensal calculada
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))

# Verifica se a prestação mensal é menor ou igual a 30% do salário do comprador
if prestacao <= minimo:
    # Se a prestação não ultrapassa o limite, o empréstimo pode ser aprovado
    print('Empréstimo pode ser CONCEDIDO!')
else:
    # Caso contrário, o empréstimo é negado
    print('Empréstimo NEGADO!')
