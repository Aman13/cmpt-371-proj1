
import sys
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Sets Host and port depending on usr arguments
host = sys.argv[1]
port = int(sys.argv[2])

#binds the socket to the correct host:port only listens to one connection at a time
serverSocket.bind((host,port))
serverSocket.listen(1)

while True:
	print "Server Started"
	connectionSocket, addr = serverSocket.accept()
	#Once accepted a connection, parses information and looks for correct file
	try:
		message = connectionSocket.recv(1024)
		requestType = message.split()[0]
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.send('HTTP/1.1 200 OK\n\n')
		#If the request is a GET must send the necessary information
		if (requestType == 'GET'):
			for i in range(0, len(outputdata)):
				connectionSocket.send(outputdata[i])
		connectionSocket.close()
	#if the file is not found, send the correct message and close the socket
	except IOError:
		connectionSocket.send('HTTP/1.1 404 Not found\n\n')
		connectionSocket.close()

serverSocket.close()