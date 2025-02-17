from .constants import SQUARE_SIZE, GREY, CROWN_PATH, WHITE_PIECE, BLACK_PIECE
from .square import Square
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == WHITE_PIECE:
            self.type = Square.WHITE_PIECE
        else:
            self.type = Square.BLACK_PIECE
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
        self.type = Square.WHITE_KING if self.color == WHITE_PIECE else Square.BLACK_KING
    
    def draw(self, window):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            CROWN = pygame.transform.scale(pygame.image.load(CROWN_PATH).convert_alpha(), (44, 25))
            CROWN.set_alpha(64)
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)