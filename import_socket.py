import socket

serverIP = "172.17.29.11"
serverPORT = 6000
serveraddress = (serverIP,serverPORT)
bufferSize = 1024
UDPClientsocket = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)
message = "now i m not coming"
bytestosend = str.encode(message)
UDPClientsocket.sendto(bytestosend,serveraddress)