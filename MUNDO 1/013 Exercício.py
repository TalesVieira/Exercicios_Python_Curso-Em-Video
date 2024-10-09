# Nome do vídeo: Reajuste Salarial
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Lê o salário do funcionário
salário = float(input('Qual é o salário do funcionário? R$ '))

# Calcula o novo salário com aumento de 15%
novo_salário = salário + (salário * 15 / 100)

# Exibe o resultado
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo_salário))
