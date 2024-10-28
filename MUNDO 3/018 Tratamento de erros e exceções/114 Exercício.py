# Nome do vídeo: Site está acessível?
# Crie um código em python que teste se o site pudim está acessível pelo compuador usado
import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O sitem pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')