# Nome do vídeo: Aumentos múltiplos
# Este programa calcula o aumento salarial de um funcionário com base no seu salário atual.
# Para salários superiores a R$1.250,00, aplica-se um aumento de 10%.
# Para salários iguais ou inferiores a R$1.250,00, aplica-se um aumento de 15%.

# Entrada de dados: Solicita ao usuário o salário atual do funcionário
salário = float(input('Qual é o salário do funcionário? R$ '))

# Verifica o valor do salário e aplica o aumento de acordo com a faixa salarial
if salário <= 1250:
    # Se o salário é igual ou menor que R$1.250,00, o aumento é de 15%
    novo = salário + (salário * 15 / 100)
else:
    # Se o salário é superior a R$1.250,00, o aumento é de 10%
    novo = salário + (salário * 10 / 100)

# Saída de dados: Exibe o salário antigo e o novo salário após o aumento
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))
