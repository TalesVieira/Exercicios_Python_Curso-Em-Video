# Nome do vídeo: Verificando as primeiras letras de um texto.
# Este programa verifica se o nome de uma cidade começa com "SANTO".

# Solicita que o usuário insira o nome de uma cidade e remove espaços extras no início e no final
cid = str(input('Em que cidade você nasceu? ')).strip()

# Converte os primeiros 5 caracteres do nome da cidade para maiúsculas e verifica se eles são iguais a 'SANTO'
print(cid[:5].upper() == 'SANTO')
