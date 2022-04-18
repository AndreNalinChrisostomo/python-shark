#importando módulos necessários
import requests
import os

#dicionário que conterá os dados do ip de destino
out = {}

def get(ip):
	global out

        #faz uma requisição para a api
	r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')

        #pega o conteúdo da página
	r = r.text
	if 'API count exceeded' in r:
		exit("API excedida")

        #cria um arquivo com a resposta da api
	with open(f'{ip}.txt', 'w') as ip_file:
		ip_file.write(r)

        #lê o arquivo e transforma a resposta em um dicionário
	with open(f"{ip}.txt", "r") as f_in:
		for line in map(str.strip, f_in):
			if not line:
				continue
			k, v = line.split(":", maxsplit=1)
			out[k.strip()] = v.strip()


        #remove o arquivo que não será mais usado
	os.remove(f'{ip}.txt')


        #printa os dados
	print(f'''
=============================
IP: {out['IP Address']}
Country: {out['Country']}
State: {out['State']}
City: {out['City']}
=============================''')









     
    
