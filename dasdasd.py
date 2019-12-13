from socket import *
import json

IPV4 = AF_INET
UDP = SOCK_DGRAM
TCP = SOCK_STREAM

def getInfo(a):
    dic, adr = skt.recvfrom(1024)

    
    new_dic = json.loads(dic.decode())
    return new_dic
def graficoTemp():

        tempo.append(i)
        #.append('')
        #arrumar um jeito de plotar as 3 temperaturas no mesmo gráfico

        aux.plot(tempo,.append) #plota gráfico de linha
        fig.canvas.draw() #atualiza o gráfico


def graficoVCC:
    #um negócio de energia aí

def graficoViscosidade:
    #gráfico de


skt = socket(IPV4,UDP)

porta = int(input("Qual porta deseja bindar? "))

skt.bind(('',porta))

while True:
    #Receber resposta

    msg, adr = skt.recvfrom(1024)
    
    dados = getInfo(msg)

    
    variaveis = dados.keys()
    i = 0
    tempo = [] 
    temperatura_extena= [] #temperatura externa
    
    temperatura_Int = [] #temperatura interna
    temp_Setada = [] #setpoint temperatura


    fig = plt.figure(1)
    aux = plt.add_subplot()
    #plt.show()

    

    time.sleep(5) #tempo de resposta de 5 segundos
    i+=1

    
    

    
    
    função(msg)
    
    
    msg = msg.encode()
    #Enviar mensagem
    skt.sendto(msg,adr)
