import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(),9500))


s.listen(5)

#Validation for the Message that is Received
while True:
    c, addr = s.accept()

    #Connection Message
    print('Got connection from ', addr)

    msg = c.recv(9500)

    #If Check to see what message is being sent
    if msg.decode("utf-8") == "Hello":
        print("Hi")
    else:
        print("Goodbye")

    c.close()