from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

host = '127.0.0.1'
port = 3000

serverSocket.bind((host,port))
serverSocket.listen(1)

while True:
	print "Server Started"
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		requestType = message.split()[0]
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.send('HTTP/1.1 200 OK\n\n')
		if (requestType == 'GET'):
			for i in range(0, len(outputdata)):
				connectionSocket.send(outputdata[i])
		connectionSocket.close()

	except IOError:
		connectionSocket.send('HTTP/1.1 404 Not found\n\n')
		connectionSocket.close()

serverSocket.close()