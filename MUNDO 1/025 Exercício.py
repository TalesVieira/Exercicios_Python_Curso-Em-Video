# Nome do vídeo: Procurando uma string dentro de outra
# Este programa verifica se o nome de uma pessoa contém a palavra "SILVA".

# Solicita que o usuário insira seu nome completo e remove quaisquer espaços extras no início e no final
nome = str(input('Qual é seu nome completo? ')).strip()

# Converte o nome para minúsculas e verifica se a palavra 'silva' está presente
# O uso de `lower()` garante que a busca não seja sensível a maiúsculas ou minúsculas
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
