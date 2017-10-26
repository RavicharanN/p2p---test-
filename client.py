import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12346

s.connect((host,port))

print "Sent by server:"
recv_data = s.recv(1024)
print(recv_data)
print "Type your message:"
send_data =raw_input()
s.send(send_data)
s.close()

# while True:
#     recv_data = s.recv(1024)
#     if not recv_data:
#         print "Connection Terminated"
#         s.close()
#     else:
#         print "Sent by server:"
#         print recv_data
#         print "Enter your message:"
#         send_data = raw_input()
#         s.send(send_data)
