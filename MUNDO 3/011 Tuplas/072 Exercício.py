# Nome do vídeo: Número por extenso
# Crie um programa que tenha uma tupla com uma contagem por extenso, de zero até vinte.
# O programa deve ler um número pelo teclado e mostrá-lo por extenso.

# Tupla com os números de 0 a 20 por extenso
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    núm = int(input('Digite um número entre 0 e 20: '))  # Solicita um número entre 0 e 20
    if 0 <= núm <= 20:  # Verifica se o número está dentro do intervalo válido
        break  # Se estiver, sai do loop
    print('Tente novamente.', end=' ')  # Mensagem para tentar novamente, caso o número esteja fora do intervalo

# Exibe o número por extenso, acessando o índice correspondente na tupla
print(f'Você digitou o número {cont[núm]}')
