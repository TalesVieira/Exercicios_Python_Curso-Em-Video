# Nome do vídeo: Contagem regressiva
# Este programa realiza uma contagem regressiva de 10 até 0, com uma pausa de 1 segundo entre cada número,
# simulando o efeito de uma contagem regressiva para o estouro de fogos de artifício.

from time import sleep  # Importa a função sleep do módulo time para adicionar pausas no programa

# Inicia a contagem regressiva de 10 até 0.
# O range(10, -1, -1) indica que o loop começará em 10 e terminará em -1 (não inclusive), com passos de -1.
for cont in range(10, -1, -1):
    print(cont)  # Exibe o valor atual da contagem regressiva
    sleep(1)     # Aguarda 1 segundo antes de continuar para o próximo número

# Após a contagem regressiva, exibe uma mensagem simulando o estouro de fogos de artifício.
print('POOOOOOOOOOOOOOOOOOOOOOOOOW')  # Imprime uma mensagem final para simbolizar os fogos de artifício
