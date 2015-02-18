import sys
from socket import *

host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]
requestType = sys.argv[4]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host,port))

clientSocket.send(requestType + ' ' + filename)
data = clientSocket.recv(1024)
print data
if (requestType == 'GET'):
	pageRequested = clientSocket.recv(1024)
	recieving = True
	while recieving == True:
		raw = clientSocket.recv(1024)
		pageRequested = pageRequested + raw
		if raw == '':
			recieving = False
	print pageRequested

clientSocket.close()