# Nome do vídeo: Formatando moedas em python
# Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais
# informando se o valor retornado por elas vai ou não ser formatado pela função moeda().

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
