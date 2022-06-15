from socket import *

serverName='192.168.137.1'
serverPort=8000

clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))

sentence=input('Input lowercase sentence:')
sentence=sentence.encode('utf-8')
clientSocket.send(sentence)
modifiedSentence=clientSocket.recv(1024)
print('From Server:',modifiedSentence)
clientSocket.close()
