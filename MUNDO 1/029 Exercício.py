# Nome do vídeo: Radar eletrônico
# Este programa lê a velocidade de um carro e verifica se ela ultrapassa o limite de 80KMH. Se ultrapassar, calcula uma multa.

# Lê a velocidade atual do carro informada pelo usuário
velocidade = float(input('Qual é a velocidade atual do carro? '))

# Verifica se a velocidade ultrapassa o limite de 80KMH
if velocidade > 80:
    # Se a condição for verdadeira, exibe a mensagem de multa
    print('MULTADO! Você excedeu o limite permitido que é de 80KMH')
    # Calcula a multa com base no excesso de velocidade (R$7,00 por km acima de 80)
    multa = (velocidade - 80) * 7
    # Exibe o valor da multa formatado para duas casas decimais
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

# Mensagem final exibida independentemente da velocidade do carro
print('Tenha um bom dia! Dirija com segurança')
