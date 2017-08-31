import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host,port)) #Connect to the server
data = s.recv(1024)
if not data  : 
	print("No data recieved")

else :
	print data #prnt the recieved message from the server
	s.close() #terminate the socket

