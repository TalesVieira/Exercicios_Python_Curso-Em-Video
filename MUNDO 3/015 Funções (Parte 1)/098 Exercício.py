# Nome do vídeo: Função de contador
# Faça um programa que tenha uma função chamada contador() que receba 3 parâmetros: início, fim e passo.
# Seu programa deve realizar três contagens:
# 1. De 1 até 10, de 1 em 1.
# 2. De 10 até 0, de 2 em 2.
# 3. Uma contagem personalizada.
from time import sleep  # Importa a função sleep para criar pausas entre os números da contagem

def contador(i, f, p):
    # Verifica se o passo é negativo, se for, converte para positivo
    if p < 0:
        p *= -1
    # Caso o passo seja zero, atribui o valor de 1 para evitar erro na contagem
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)  # Pausa de 2.5 segundos antes de começar a contagem

    # Se o início for menor que o fim, faz a contagem crescente
    if i < f:
        cont = i  # Inicializa o contador com o valor de início
        while cont <= f:  # Continua até o valor final
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)  # Pausa de 0.5 segundos entre os números
            cont += p  # Incrementa o contador pelo valor de passo
        print('FIM!')  # Exibe "FIM!" ao final da contagem
    # Se o início for maior que o fim, faz a contagem regressiva
    else:
        cont = i  # Inicializa o contador com o valor de início
        while cont >= f:  # Continua até o valor final
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)  # Pausa de 0.5 segundos entre os números
            cont -= p  # Decrementa o contador pelo valor de passo
        print('FIM!')  # Exibe "FIM!" ao final da contagem

# Primeira contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)
# Segunda contagem de 10 até 0, de 2 em 2
contador(10, 0, 2)

# Solicita ao usuário para personalizar a contagem
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

# Chama a função contador com os valores personalizados
contador(ini, fim, passo)
