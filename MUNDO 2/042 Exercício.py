# Nome do vídeo: Analisando Triângulos v2.0
# Este programa determina se três segmentos de reta podem formar um triângulo e, se possível,
# classifica o triângulo em Equilátero, Isósceles ou Escaleno.

# Lê o comprimento dos três segmentos
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se os segmentos podem formar um triângulo, aplicando a condição da existência de triângulos
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end=' ')
    # Classifica o triângulo como Equilátero, Isósceles ou Escaleno
    if r1 == r2 == r3:
        # Todos os lados iguais
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        # Todos os lados diferentes
        print('ESCALENO!')
    else:
        # Dois lados iguais
        print('ISÓSCELES!')
else:
    # Os segmentos não formam um triângulo
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
