# PythonShark
Python Shark foi uma ideia que tive após mexer por alguns minutos em um desses rastreadores de endereços IP, vi muitas pessoas pregando peças em chats online de vídeos, por isso decidi fazer minha própria ferramenta para isso. 
## como funciona?
O programa usa o módulo pyshark (como pode ver não sou muito criativo para nomes) que embrulha o programa TShark, uma versão linha de comando do gerenciador de pacotes de dados Wireshark (por conta disso, o programa aceita os mesmos filtros do Wireshark)  para analisar os pacotes que circulam no seu computador. 
O programa então pega apenas o endereço IP do pacote que foi recebido e joga dentro de uma API do site https://hackertarget.com/ para rastrear o IP 
O programa também conta com um sistema simples para impedir que IPs repetidos apareçam 

## observações
* O programa precisa ser executado em uma pasta onde ele tenha permissão para criar e deletar arquivos.

* Testei-o ambos nos sistemas operacionais Windows e Linux, por motivos desconhecidos, o programa só funciona com perfeição no sistema Windows 

