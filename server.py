import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname() # Get local machine host
port = 12345 # Reserve a port for your operation

s.bind((host,port)) 
s.listen(5) # Terminate after 5 requests

while True :
	(client_thread, address) = s.accept() 
	print "connected to client. Address:",address
	client_thread.send("Thank You. Connection Established") # Send a message to the client
	client_thread.close()