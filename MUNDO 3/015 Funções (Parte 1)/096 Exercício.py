# Nome do vídeo: Função que calcula área
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# largura e comprimento e mostre a área do terreno

def área(larg, comp):
    """Função que calcula a área de um terreno retangular.
    
    Recebe como parâmetros a largura e o comprimento do terreno e calcula a área,
    que é dada pelo produto da largura pelo comprimento.
    """
    a = larg * comp  # Calcula a área multiplicando a largura pelo comprimento
    print(f'A área de um terreno {larg}X{comp} é de {a}m²')  # Exibe o resultado formatado com as dimensões e a área

# Programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))  # Solicita ao usuário a largura do terreno
c = float(input('COMPRIMENTO (m): '))  # Solicita ao usuário o comprimento do terreno
área(l, c)  # Chama a função área() passando os valores de largura e comprimento
