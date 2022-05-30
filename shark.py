from api import get
#from api import ip_only
import pyshark

#modifique estas variáveis
seu_ip_interno = '192.168.0.13'
iface = 'Wi-Fi'


#inicia a captura em Live
capture = pyshark.LiveCapture(interface=iface,display_filter=input("filtro: "))


#lista de IPs que ja foram exibidos (não está funcionando, estou tentando descobrir o porquê)
vistos = []


def start():
	#loop pelos pacotes que estão sendo capturados
	for packet in capture.sniff_continuously():
		#se o seu computador for a fonte do pacote
		if seu_ip_interno in str(packet.ip.dst):
			#verifica se o destino do pacote já está na lista
			if str(packet.ip.src) in vistos:
				pass
			else:
				if seu_ip_interno in str(packet.ip.src):
					pass
				else:
					#tenta rastrear o ip do pacote
					get(str(packet.ip.src))
					#ip_only(str(packet.ip.src))
					

				# adiciona o ip de destino na lista 'vistos'
				vistos.append(str(packet.ip.src))
	#fecha a captura
	capture.close()

#inicia
start()
