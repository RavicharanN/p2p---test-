import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12346

print "WAiting for connection"
s.bind((host,port))
s.listen(5)

client,address = s.accept()
print "Connection Esatablished"
print "Enter your message"
send_data = raw_input()
client.send(send_data)
recv_data = client.recv(1024)
print "Sent by client :"
print(recv_data)

#
# while True:
#     (client_thread,address) = s.accept()
#     print "Recieved from client" + address + ":"
#     recv_data = client_thread.recv(1024)
#     print(recv_data)
#     print "Enter Mesaage:"
#     s = raw_input()
#     client_thread.send(s)
