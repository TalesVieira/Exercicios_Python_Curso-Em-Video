# Nome do vídeo: Validando entrada de dados em Python
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input do Python,
# mas fazendo a validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaInt('Digite um número: ')

def leiaInt(msg):
    """
    -> Função que lê um número inteiro com validação.
    :param msg: Mensagem de solicitação de entrada.
    :return: O valor numérico validado como inteiro.
    """
    ok = False  # Variável de controle para saber se a entrada é válida
    valor = 0  # Variável para armazenar o número inteiro convertido
    while True:
        n = input(msg)  # Solicita a entrada do usuário
        if n.isnumeric():  # Verifica se a entrada é numérica
            valor = int(n)  # Converte a entrada para inteiro
            ok = True  # Marca como válido para interromper o loop
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')  # Mensagem de erro para entrada inválida
        if ok:
            break  # Sai do loop se a entrada for válida
    return valor  # Retorna o valor convertido para inteiro

# Programa principal
n = leiaInt('Digite um número: ')  # Chama a função leiaInt com a mensagem de entrada
print(f'Você acabou de digitar o número {n}')  # Exibe o número digitado pelo usuário
