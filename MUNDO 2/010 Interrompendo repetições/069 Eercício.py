# Nome do vídeo: Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas. Para cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# - Quantas pessoas têm mais de 18 anos
# - Quantos homens foram cadastrados
# - Quantas mulheres têm menos de 20 anos

tot18 = totH = totM20 = 0  # Variáveis para contadores

while True:
    idade = int(input('Idade: '))  # Recebe a idade da pessoa
    sexo = ' '
    while sexo not in 'MF':  # Valida a entrada de sexo
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
    # Verifica e conta as condições
    if idade >= 18:  # Conta pessoas com 18 anos ou mais
        tot18 += 1
    if sexo == 'M':  # Conta homens
        totH += 1
    if sexo == 'F' and idade < 20:  # Conta mulheres com menos de 20 anos
        totM20 += 1
    
    # Pergunta se o usuário quer continuar cadastrando
    resp = ' '
    while resp not in 'SN':  # Valida a resposta do usuário
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':  # Interrompe o loop se o usuário escolher 'N'
        break

# Exibe os resultados finais
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
