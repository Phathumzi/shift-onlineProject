import socket
import pygame
import pickle
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, DARK_GREY
from checkers.game import Game

FPS = 60
pygame.display.set_caption('Player 2: GREY')

#Create client socket and connect to server (player 1)
Server_Addr = (socket.gethostbyname(socket.gethostname()), 5050)
client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Server_Addr)

#send updated board to player 1
def sendBoard(board):
    client.send(pickle.dumps(board))

#Receive updated board from player 1
def receiveBoard():
    board = pickle.loads(client.recv(4096))
    return board

#Get mouse location
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    
    #intialise game
    game = Game(pygame.display.set_mode((WIDTH, HEIGHT)))
    game.update()
    game.turn = DARK_GREY
    board = receiveBoard()
    game.board.updateBoard(board)
    game.update()

    while run:
        clock.tick(FPS)

        if game.winner() != None: #check if someone won the game
            print(game.winner())
            run = False
        
        for event in pygame.event.get():  #detects for when the window is closed
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: #detects for when the mouse is pressed
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        if game.moved:
            #after making a move, send the updated board to player 1
            sendBoard(game.board.board)
            game.change_turn()
            #after player 1 makes a move, receive the updated board sent by player 1
            board = receiveBoard()
            game.board.updateBoard(board)
            game.update()
            
main()