# Nome do vídeo: Funções para votação
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date  # Importa a função date para obter o ano atual
    atual = date.today().year  # Pega o ano atual
    idade = atual - ano  # Calcula a idade da pessoa com base no ano de nascimento
    # Verifica a idade e determina a categoria de votação
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'  # Menores de 16 anos não votam
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'  # Voto é opcional para pessoas entre 16-18 ou acima de 65 anos
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'  # Voto obrigatório para pessoas entre 18 e 65 anos

# Solicita o ano de nascimento ao usuário e exibe a categoria de votação
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))  # Chama a função voto e imprime o resultado
