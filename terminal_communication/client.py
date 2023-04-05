import socket

Disconnect_Message = "!Disconnected"
Turn_Message = "Your turn"
Wait_Message = "Wait, other player's turn"

# Create client socket and connect to server
Server_Addr = (socket.gethostbyname(socket.gethostname()), 5050)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Server_Addr)
print(client.recv(2048).decode())  # which player am I?

# send messages to server


def send(msg):
    client.send(str.encode(msg))


def firstBoard():
    board = [["0", "1", "2", "3", "4", "5", "6", "7", "8"],
             ["1", "-", "#", "-", "#",  "-", "#",  "-", "#"],
             ["2", "#", "-", "#",  "-", "#",  "-", "#", "-"],
             ["3", "-", "#", "-", "#",  "-", "#",  "-", "#"],
             ["4", "-", "-", "-", "-",  "-", "-",  "-", "-"],
             ["5", "-", "-", "-", "-",  "-", "-",  "-", "-"],
             ["6", "&", "-", "&",  "-", "&",  "-", "&", "-"],
             ["7", "-", "&", "-",  "&", "-",  "&", "-", "&"],
             ["8", "&", "-", "&",  "-", "&",  "-", "&", "-"],

             ]
    count = 0
    while count < 9:
        for i in board[count]:
            print(i, end=" ")

        print('\n')
        count += 1


def updatedBord(row, col, moveToROW, moveToCOL):  # used to edit board

    board = [["0", "1", "2", "3", "4", "5", "6", "7", "8"],
             ["1", "-", "#", "-", "#",  "-", "#",  "-", "#"],
             ["2", "#", "-", "#",  "-", "#",  "-", "#", "-"],
             ["3", "-", "#", "-", "#",  "-", "#",  "-", "#"],
             ["4", "-", "-", "-", "-",  "-", "-",  "-", "-"],
             ["5", "-", "-", "-", "-",  "-", "-",  "-", "-"],
             ["6", "&", "-", "&",  "-", "&",  "-", "&", "-"],
             ["7", "-", "&", "-",  "&", "-",  "&", "-", "&"],
             ["8", "&", "-", "&",  "-", "&",  "-", "&", "-"],
             ]

    board[moveToROW][moveToCOL] = board[row][col]
    board[row][col] = "-"
    count = 0

    while count < 9:
        for i in board[count]:
            print(i, end=" ")

        print('\n')
        count += 1


def main():
    print(client.recv(2048).decode())  # game has started
    # print(client.recv(2048).decode())

    print("\n")
    print(firstBoard())
    run = True

    while run:
        myTurn = client.recv(2048).decode()
        print(myTurn)
        if myTurn == Turn_Message:

            row = input("which ROW do you want to move-  ")
            col = input("which COL is the piece-   ")
            moveToROW = input("which ROW do you want to MOVE IT TO-  ")
            moveToCOL = input("Which COLUMN do you want to MOVE IN TO-  ")

            # send(updatedBord(row, col, moveToROW, moveToCOL))

            # send(input())
            send("YOUR OPONENT MOVED " + "(" + row + "," + col + ")" +
                 " TO " + "(" + moveToROW + "," + moveToCOL + ")")

            updatedBord(int(row), int(col), int(moveToROW), int(moveToCOL))

            # send(updatedBord())


main()
