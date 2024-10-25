# Nome do vídeo: Função para fatorial
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indica o número a calcular
# e o outro chamado show, que será um valor lógico opcional indicando se será mostrado ou não na tela o processamento do cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de n.
    """
    
    f = 1  # Inicializa a variável f com 1, que será usada para o cálculo do fatorial
    for c in range(n, 0, -1):  # Loop que vai de n até 1 (inclusive), decrementando 1 a cada passo
        if show:  # Se show for True, exibe o processo de cálculo
            print(c, end='')  # Exibe o número atual no cálculo
            if c > 1:
                print(' X ', end='')  # Exibe o símbolo de multiplicação se houver mais números a multiplicar
            else:
                print(' = ', end='')  # Exibe o símbolo de igualdade antes do resultado final

        f *= c  # Multiplica o valor de f pelo número atual (c) para calcular o fatorial
    return f  # Retorna o valor final do fatorial

# Exemplo de uso da função fatorial com o parâmetro show=True para exibir o cálculo
print(fatorial(5, show=True))
# Exibe a documentação da função fatorial usando a função help()
help(fatorial)
