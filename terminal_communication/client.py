import socket

Disconnect_Message = "!Disconnected"
Turn_Message = "Your turn"
Wait_Message = "Wait, other player's turn"

#Create client socket and connect to server
Server_Addr = (socket.gethostbyname(socket.gethostname()), 5050)
client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Server_Addr)
print(client.recv(2048).decode()) #which player am I?

#send messages to server
def send(msg):
    client.send(str.encode(msg))


def main():
    print(client.recv(2048).decode()) #game has started
    run = True

    while run:
        myTurn = client.recv(2048).decode()
        print(myTurn)
        if myTurn == Turn_Message:
            send(input())


main()