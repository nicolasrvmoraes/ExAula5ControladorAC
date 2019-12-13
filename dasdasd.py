from socket import *
import json

IPV4 = AF_INET
UDP = SOCK_DGRAM
TCP = SOCK_STREAM

def getInfo(a):
    dic, adr = skt.recvfrom(1024)

    
    new_dic = json.loads(dic.decode())
    return new_dic



skt = socket(IPV4,UDP)

porta = int(input("Qual porta deseja bindar? "))

skt.bind(('',porta))

while True:
    #Receber resposta

    msg, adr = skt.recvfrom(1024)
    
    dados = getInfo(msg)

    
    
    

    
    
    função(msg)
    
    
    msg = msg.encode()
    #Enviar mensagem
    skt.sendto(msg,adr)
