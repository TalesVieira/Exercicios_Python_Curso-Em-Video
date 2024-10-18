# Nome do vídeo: Lista ordenada sem repetições
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção, sem usar o sort().
# No final, mostre a lista ordenada na tela.

# Inicializando uma lista vazia
lista = []

# Loop para solicitar ao usuário cinco valores
for c in range(0, 5):
    n = int(input('Digite um valor: '))  # Solicita ao usuário que digite um valor numérico
    
    # Se for o primeiro valor ou se o valor digitado for maior que o último valor da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)  # Adiciona o valor ao final da lista
        print('Adicionado ao final da lista...')
    else:
        # Se o valor não for o maior, procurar a posição correta para inseri-lo
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:  # Verifica se o valor deve ser inserido nessa posição
                lista.insert(pos, n)  # Insere o valor na posição correta
                print(f'Adicionado na posição {pos} da lista...')
                break  # Sai do loop após inserir o valor
            pos += 1  # Continua verificando as posições

# Exibe uma linha de separação
print('-=' * 30)

# Exibe a lista final com os valores digitados em ordem
print(f'Os valores digitados em ordem foram {lista}')
