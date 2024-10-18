# Nome do vídeo: Validando expressões matemáticas
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Lê a expressão digitada pelo usuário
expr = str(input('Digite a expressão: '))

# Inicializa uma lista chamada 'pilha' para simular o funcionamento de uma pilha de parênteses
pilha = []

# Itera por cada símbolo da expressão
for símb in expr:
    # Se o símbolo for um parêntese de abertura '(', ele é adicionado à 'pilha'
    if símb == '(':
        pilha.append('(')
    # Se o símbolo for um parêntese de fechamento ')', o programa verifica:
    elif símb == ')':
        # Se houver um parêntese de abertura na pilha, ele é removido, pois foi "fechado"
        if len(pilha) > 0:
            pilha.pop()  # Remove o último parêntese de abertura da pilha
        # Se não houver parêntese de abertura na pilha, adiciona o parêntese de fechamento para marcar erro
        else:
            pilha.append(')')
            break  # Interrompe o loop, pois já sabemos que a expressão está incorreta

# Após o loop, se a pilha estiver vazia, todos os parênteses foram fechados corretamente
if len(pilha) == 0:
    print('Sua expressão está válida!')
# Caso contrário, existem parênteses desbalanceados
else:
    print('Sua expressão está errada!')
