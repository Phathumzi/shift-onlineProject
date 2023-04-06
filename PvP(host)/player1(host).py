import socket
import pygame
import pickle
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60
pygame.display.set_caption('Player 1: RED')

#Create an address for the server (IP address, port number)
Addr = (socket.gethostbyname(socket.gethostname()), 5050)

#Create socket and bind it to address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Addr)


class Client():
    def __init__(self, num):
        self.conn, self.addr = server.accept()
        self.num = num
        print(f"[New Connection] {self.addr} is now connected!")
        print(f"[Active Connections]  {num} ")

    #Send updated board to player
    def sendBoard(self, board):
        self.conn.send(pickle.dumps(board))

    #Receive updated board from player
    def receiveBoard(self):
        board = pickle.loads(self.conn.recv(2048))
        return board

#Get mouse location
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    #Starts server: listens for new connections and store client info
    print("[Starting] Server has now started")
    print("[Listening] Server is listening for new connections")
    ConnCount = 0
    server.listen()
    run = False

    #Create player 2
    ConnCount += 1
    player2 = Client(ConnCount)
    
    #Start Game
    if ConnCount == 1:
        run = True
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() != None: #check if someone won the game
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #detects for when the window is closed
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #detects for when the mouse is pressed
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        if game.moved:
            #after making a move, send the updated board to player 2
            player2.sendBoard(game.board.board)
            game.change_turn()
            #after player 2 makes a move, receive the updated board sent by player 2
            board = player2.receiveBoard()
            game.board.updateBoard(board)
            game.update()

main()