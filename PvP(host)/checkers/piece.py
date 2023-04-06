from .constants import RED, SQUARE_SIZE, GREY, MAROON #, CROWN
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

        if self.color == RED:
            self.border_color = MAROON
        else:
            self.border_color = GREY


    def calc_pos(self):
        #calculates postion to place each piece in the center of its square 
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, self.border_color, (self.x, self.y), radius + self.OUTLINE) #draw nice grey outline over the piece
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) #draw the piece
        #if self.king: #draw crown
        #    win.blit(CROWN, (self.x - CROWN.get_width()//2, (self.y - CROWN.get_height()//1.80)))

    def move(self, row, col):
        #when a move is made track the piece's new location
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)