def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()  # Cria um dicionário para armazenar os resultados
    r['total'] = len(n)  # Quantidade total de notas recebidas
    r['maior'] = max(n)  # Maior nota recebida
    r['menor'] = min(n)  # Menor nota recebida
    r['média'] = sum(n) / len(n)  # Média das notas
    
    if sit:  # Se o parâmetro sit for True, adiciona a situação da turma
        if r['média'] >= 7:
            r['situação'] = 'BOA'  # Situação é 'BOA' se a média for 7 ou mais
        elif r['média'] > 5:
            r['situação'] = 'RAZOÁVEL'  # Situação é 'RAZOÁVEL' se a média estiver entre 5 e 7
        else:
            r['situação'] = 'RUIM'  # Situação é 'RUIM' se a média for abaixo de 5
    return r  # Retorna o dicionário com os resultados

# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)  # Chama a função com notas e situação habilitada
print(resp)  # Exibe o dicionário com os resultados
help(notas)  # Exibe a docstring da função usando help()
