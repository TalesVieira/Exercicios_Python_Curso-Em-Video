def aumentar(preço, taxa):
    # Calcula o valor aumentado pela taxa percentual especificada
    res = preço + (preço * taxa / 100)
    return res  # Retorna o valor com o aumento aplicado

def diminuir(preço, taxa):
    # Calcula o valor reduzido pela taxa percentual especificada (erro corrigido para divisão por 100)
    res = preço - (preço * taxa / 100)
    return res  # Retorna o valor com a redução aplicada

def dobro(preço):
    # Calcula o dobro do valor informado
    res = preço * 2
    return res  # Retorna o valor dobrado

def metade(preço):
    # Calcula a metade do valor informado
    res = preço / 2
    return res  # Retorna o valor reduzido à metade
