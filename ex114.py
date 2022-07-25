import urllib
import urllib.request
sitep = 'http://pudim.com.br/'

try:
    site = urllib.request.urlopen(sitep)
except not urllib.error.URLError:
    print(f'O site {sitep} não está acessível no momento.')
else:
    print(f'O site {sitep} está acessível no momento.')