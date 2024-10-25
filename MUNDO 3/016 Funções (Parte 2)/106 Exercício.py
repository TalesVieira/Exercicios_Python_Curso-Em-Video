# Nome do vídeo: Sistema interativo de ajuda em python
# Faça um mini sistema que utilize o interactive help do python, o usuário vai digitar o comando e o manual vai aparecer
# Quando o usuário digitar a palavra 'FIM' o programa se encerrará

from time import sleep

# Define as cores em uma lista, para usar nos títulos e mensagens
c = ('\033[m',  # 0 - Sem cor
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 3 - Amarelo
     '\033[0;30;44m',  # 4 - Azul
     '\033[0;30;45m',  # 5 - Roxo
     '\033[7;30m')  # 6 - Branco

def ajuda(com):
    """
    Exibe o manual de ajuda do Python para o comando passado.
    :param com: Comando ou biblioteca do qual se quer ver a documentação.
    """
    título(f'Acessando o manual do comando \'{com}\'', 4)  # Chama o título com a cor azul (índice 4)
    print(c[6], end='')  # Muda para a cor branca
    help(com)  # Exibe o manual de ajuda do Python para o comando passado
    print(c[0], end='')  # Volta para a cor padrão
    sleep(2)  # Pausa de 2 segundos para a leitura do manual

def título(msg, cor=0):
    """
    Exibe um título formatado com uma borda ao redor.
    :param msg: Mensagem que será exibida.
    :param cor: Cor do título (índice da lista c).
    """
    tam = len(msg) + 4  # Calcula o tamanho do título com borda
    print(c[cor], end='')  # Muda para a cor especificada
    print('*' * tam)  # Imprime a borda superior
    print(f'  {msg}  ')  # Imprime a mensagem com borda lateral
    print('*' * tam)  # Imprime a borda inferior
    print(c[0], end='')  # Volta para a cor padrão
    sleep(1)  # Pausa de 1 segundo para exibir o título

# Programa Principal
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)  # Exibe o título principal em verde (índice 2)
    comando = str(input('Função ou Biblioteca > '))  # Solicita ao usuário um comando ou biblioteca
    if comando.upper() == 'FIM':  # Se o usuário digitar 'FIM', o loop termina
        break
    else:
        ajuda(comando)  # Chama a função ajuda() com o comando fornecido

título('ATÉ LOGO', 1)  # Exibe a mensagem de saída em vermelho (índice 1)
