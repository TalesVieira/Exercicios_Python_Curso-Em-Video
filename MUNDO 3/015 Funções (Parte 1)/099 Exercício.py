# Nome do vídeo: Função que descobre o maior
# Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep  # Importa a função sleep para criar pausas durante a análise dos valores

def maior(*núm):
    cont = maior = 0  # Inicializa as variáveis cont (contador) e maior (maior valor)
    print('-=' * 30)
    print('Analisando os valores passados...')

    # Loop para percorrer todos os valores passados como argumento
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)  # Pausa de 0.3 segundos entre a exibição dos números
        # Na primeira iteração, o primeiro valor é considerado o maior
        if cont == 0:
            maior = valor
        else:
            # Se o valor atual for maior que o maior valor encontrado até agora, atualiza a variável maior
            if valor > maior:
                maior = valor
        cont += 1  # Incrementa o contador a cada iteração

    # Após o loop, exibe o número de valores informados e o maior valor
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# Chamada da função com diferentes conjuntos de valores para teste
maior(2, 9, 4, 5, 6, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()  # Chamada sem valores, o que testaria o comportamento da função nesse caso
