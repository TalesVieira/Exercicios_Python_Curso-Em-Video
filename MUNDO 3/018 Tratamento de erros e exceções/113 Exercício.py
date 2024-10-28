# Nome do vídeo: Funções aprofundadas em python
# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaInt(msg):
    # Inicia um loop infinito para garantir que uma entrada válida seja recebida
    while True:
        try:
            # Tenta converter a entrada do usuário para um número inteiro
            n = int(input(msg))
        except (ValueError, TypeError):
            # Se ocorrer um erro de valor ou tipo, exibe uma mensagem de erro
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue  # Reinicia o loop
        except KeyboardInterrupt:
            # Se o usuário interromper a entrada, exibe uma mensagem e retorna 0
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0 
        else:
            # Se a entrada for válida, retorna o valor convertido
            return n
        

def leiaFloat(msg):
    # Inicia um loop infinito para garantir que uma entrada válida seja recebida
    while True:
        try: 
            # Tenta converter a entrada do usuário para um número de ponto flutuante
            n = float(input(msg))
        except (ValueError, TypeError):
            # Se ocorrer um erro de valor ou tipo, exibe uma mensagem de erro
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue  # Reinicia o loop
        except KeyboardInterrupt:
            # Se o usuário interromper a entrada, exibe uma mensagem e retorna 0
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0 
        else:
            # Se a entrada for válida, retorna o valor convertido
            return n 
        

# Solicita ao usuário que insira um número inteiro, usando a função leiaInt()
n1 = leiaInt('Digite um inteiro: ')
# Solicita ao usuário que insira um número real, usando a função leiaFloat()
n2 = leiaFloat('Digite um real: ')
# Exibe os valores inteiros e reais fornecidos pelo usuário
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')
