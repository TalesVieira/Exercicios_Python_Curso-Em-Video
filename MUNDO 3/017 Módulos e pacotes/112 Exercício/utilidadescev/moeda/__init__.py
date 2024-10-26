def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Aumenta o preço em uma taxa especificada.
    :param preço: O preço original.
    :param taxa: A taxa de aumento.
    :param formato: Indica se o resultado deve ser formatado como moeda.
    :return: O preço aumentado, formatado se especificado.
    """
    res = preço + (preço * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Diminui o preço em uma taxa especificada.
    :param preço: O preço original.
    :param taxa: A taxa de diminuição.
    :param formato: Indica se o resultado deve ser formatado como moeda.
    :return: O preço diminuído, formatado se especificado.
    """
    res = preço - (preço * taxa / 100)
    return res if not formato else moeda(res)

def dobro(preço=0, formato=False):
    """
    -> Calcula o dobro do preço.
    :param preço: O preço original.
    :param formato: Indica se o resultado deve ser formatado como moeda.
    :return: O dobro do preço, formatado se especificado.
    """
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0, formato=False):
    """
    -> Calcula a metade do preço.
    :param preço: O preço original.
    :param formato: Indica se o resultado deve ser formatado como moeda.
    :return: A metade do preço, formatada se especificado.
    """
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço=0, simbolo='R$'):
    """
    -> Formata um valor monetário.
    :param preço: O valor a ser formatado.
    :param simbolo: O símbolo da moeda.
    :return: O valor formatado como moeda.
    """
    return f'{simbolo}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    """
    -> Exibe um resumo com informações sobre o preço, incluindo aumento e diminuição.
    :param preço: O preço a ser analisado.
    :param taxaa: A taxa de aumento.
    :param taxar: A taxa de redução.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)

# Exemplo de uso da função resumo
resumo(100)
