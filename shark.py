from api import get_location, ip_only, menu
import pyshark

#modifique estas variáveis
seu_ip_interno = '192.168.0.13'
iface = 'Wi-Fi'


#inicia a captura em Live
capture = pyshark.LiveCapture(interface=iface,display_filter=input("filtro: "))


vistos = []


def start():
	opcao_repeticoes = 0
	opcao = 0
	print("""
		======================
		1 - pegar localização
		2 - pegar ip
		3 - sair
		======================""")

	escolha = input("digite a opção: ")

	if escolha == "1":
		opcao = 1
	elif escolha == "2":
		opcao = 2
	elif opcao == "3":
		opcao = 3

	print("""
		======================
		Evitar repetições?
		1 - Sim
		2 - Não
		======================""")
	escolha_repeticoes = input("digite a opção: ")
	
	if escolha_repeticoes == "1":
		opcao_repeticoes = 1
	elif escolha_repeticoes == "2":
		opcao_repeticoes = 2
	else:
		exit("opção inválida")
		




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
					#executa a função escolhida pelo usuário
					if opcao == 1:
					
						get_location(str(packet.ip.src))
					elif opcao == 2:
						
						ip_only(str(packet.ip.src))
					elif opcao == 3:
						exit("saindo...")			

				# adiciona o ip de destino na lista 'vistos'
				if opcao_repeticoes == 1:
					vistos.append(str(packet.ip.src))
				else:
					pass
	#fecha a captura
	capture.close()

#inicia
start()
