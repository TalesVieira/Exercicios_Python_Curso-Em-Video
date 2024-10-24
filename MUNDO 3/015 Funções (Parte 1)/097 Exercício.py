# Nome do vídeo: Um print especial
# Faça um programa que tenha função chamada escreva, que receba um texto qualquer como parâmetro e mostre uma 
# Mensagem com tamanho adaptável 

def escreva(msg):
    # Calcula o tamanho da mensagem adicionando 4 para deixar espaço nas bordas de '~'
    tam = len(msg) + 4
    # Imprime a borda superior da caixa, com o comprimento adaptado ao tamanho da mensagem
    print('~' * tam)
    # Imprime a mensagem centralizada, com um espaço em branco antes e depois da string
    print(f' {msg}')
    # Imprime a borda inferior da caixa, igual à superior
    print('~' * tam)

# Chama a função 'escreva' passando diferentes mensagens, que ajusta o tamanho da borda automaticamente
escreva('Gustavo Guanabara')
escreva('Curso de python no YouTube')
escreva('CeV')
