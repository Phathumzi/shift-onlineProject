import socket

Disconnect_Message = "!Disconnected"
Turn_Message = "Your turn"
Wait_Message = "Opponent's turn"


# Create an address for the server (IP address, port number)
Addr = (socket.gethostbyname(socket.gethostname()), 5050)

# Create socket and bind it to address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Addr)


# send message to 1 client
def send(message, client):
    client.conn.send(str.encode(message))


# send message to both clients
def sendAll(message, client1, client2):
    client1.conn.send(str.encode(message))
    client2.conn.send(str.encode(message))


class Client():
    def __init__(self, num):
        self.conn, self.addr = server.accept()
        self.num = num
        print(f"[New Connection] {self.addr} is now connected!")
        print(f"[Active Connections]  {num} ")
        send(f"Hello, you are player {num}", self)

    # Receive message from new client
    def receiveMsg(self):
        msg = self.conn.recv(2048).decode()
        print(f"[Message received from player {self.num}] : {msg}")
        return msg


# Handles who's turn it is
def YourTurn(client1, client2):
    send(Turn_Message, client1)
    move = client1.receiveMsg()
    send(Wait_Message, client1)
    # send move to other player
    send(f"Opponent has played: '\n' {move}", client2)


def main():
    # Starts server: listens for new connections and store client info
    print("[Starting] Server has now started")
    print("[Listening] Server is listening for new connections")
    ConnCount = 0
    server.listen()
    run = True

    # Create player 1 & 2
    ConnCount += 1
    player1 = Client(ConnCount)
    send("Waiting to find player 2", player1)
    ConnCount += 1
    player2 = Client(ConnCount)

    # Start Game
    startGame = "[Started Game] Let the battle, begin!"
    print(startGame)
    sendAll(startGame, player1, player2)
    send(Wait_Message, player2)
    while run:
        YourTurn(player1, player2)
        YourTurn(player2, player1)


main()
