import sys
from socket import *

#User inputed arguments to specify host, port, file name and request type
host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]
requestType = sys.argv[4]
clientSocket = socket(AF_INET, SOCK_STREAM)

#connects to port given by user arguments
clientSocket.connect((host,port))
#sends the request in the proper format
clientSocket.send(requestType + ' ' + filename)
data = clientSocket.recv(1024)
#outputs the servers response
print data
#Need to check the response to see if there is a file to download
fileExist = data.split()[1]
if (requestType == 'GET' and fileExist == '200'):
	#creates a new file to download the requested file
	newFile = open ('download_' + filename[1:], 'wb')
	pageRequested = clientSocket.recv(1024)
	recieving = True
	#loop to make sure all the information is collected
	while recieving == True:
		raw = clientSocket.recv(1024)
		pageRequested = pageRequested + raw
		if raw == '':
			recieving = False
	#prints the information recieved on GET requests
	print pageRequested
	newFile.write(pageRequested)

clientSocket.close()