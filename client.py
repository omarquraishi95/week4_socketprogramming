import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(),9500))

#While Running the Program Simply Change the Client Message and Run the Program in the Terminal You notice the Message Changes
#When the Client Message is something different than Hello

clientMessage = "Hello"

s.sendall(clientMessage.encode())

s.close()