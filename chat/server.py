import socket

CHUNK = 65535 #receive at most these bytes of data at once

port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#create a socket object #socket.socket(family, type)

#AF_INET : family of ipv4 ip address
# socket.SOCK_DGRAM : UDP , SOCK_STREAM : TCP
#some ip address that the server will listen to when message comes

hostname = '127.0.0.1' #ip add of local machine, same for everyone

s.bind((hostname, port)) #bind the socket with this hot machine and on port 3000

print(f"server is live on {s.getsockname()}")

#run this server infinitely, till i stop manually

while True: #infinite loop
    data,clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii') # data by default travels in bytes
    print(f"Shruti: {message}")
    message_send = input("Reply: ")
    data = message_send.encode("ascii")
    # send data to the ip add that sent me the data
    s.sendto(data,clientAdd)