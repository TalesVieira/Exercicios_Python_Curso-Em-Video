def aumentar(preço=0, taxa=0):
    # Calcula o valor aumentado pela taxa percentual especificada
    res = preço + (preço * taxa / 100)
    return res  # Retorna o valor com o aumento aplicado

def diminuir(preço=0, taxa=0):
    # Calcula o valor reduzido pela taxa percentual especificada
    res = preço - (preço * taxa / 100)
    return res  # Retorna o valor com a redução aplicada

def dobro(preço=0):
    # Calcula o dobro do valor informado
    res = preço * 2
    return res  # Retorna o valor dobrado

def metade(preço=0):
    # Calcula a metade do valor informado
    res = preço / 2
    return res  # Retorna o valor reduzido à metade

def moeda(preço=0, moeda='R$'):
    # Formata o valor como moeda, com duas casas decimais e substitui '.' por ','
    return f'{moeda}{preço:.2f}'.replace('.', ',')
