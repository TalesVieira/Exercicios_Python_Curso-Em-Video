# Nome do vídeo: Progressão aritmética
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA 
# no final mostre os 10 primeiros termos dessa progressão

# Lê o primeiro termo da PA e a razão da progressão aritmética
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

# Calcula o décimo termo da PA usando a fórmula do enésimo termo
décimo = primeiro + (10 - 1) * razão

# Laço for para gerar e exibir os 10 primeiros termos da PA
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')  # Imprime cada termo da PA na mesma linha, separado por '->'

print('ACABOU')  # Mensagem final indicando o fim da sequência
