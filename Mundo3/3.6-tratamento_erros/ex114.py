from os import link
import string
import requests

def checaSite(site=string):
    try:
        get = requests.get(site)
        if get.status_code == 200:
            return(f"\033[1;32;47m O site pudim.com.br é acessível!")
        else:
            return(f"\033[1;31;40m O site pudim.com.br está com problemas!")
    except requests.exceptions.ConnectionError as erro:
        raise SystemExit(f"\033[1;31,40m O site pudim.com.br não pode ser acessado!")

print(checaSite('http://pudim.com.br/'))