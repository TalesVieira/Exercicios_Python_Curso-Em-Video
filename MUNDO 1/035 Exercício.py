# Nome do vídeo: Analisando triângulo v1.0
# Este programa verifica se três segmentos de reta podem formar um triângulo.
# Para que os segmentos formem um triângulo, a soma de dois deles deve ser sempre maior que o terceiro.

# Exibe uma linha de separação e o título do programa
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

# Entrada de dados: Solicita ao usuário os comprimentos dos três segmentos de reta
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se os segmentos podem formar um triângulo usando a condição do triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    # Se a condição é verdadeira, os segmentos podem formar um triângulo
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    # Caso contrário, os segmentos não podem formar um triângulo
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')
