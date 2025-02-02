import sys
import pygame
import numpy as np
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("This is my tic tac toe AI")
screen.fill(BG_COLOR)

class Board:
  def __init__(self):
    self.squares = np.zeros((ROWS,COLUMNS))
    
  def mark_sqr(self,row,col,player):
    self.squares[row][col]=player

  def empty_sqr(self,row,col):
    return self.squares[row][col]==0
  
class Game:
  def __init__(self):
    self.board = Board()
    self.player = 1
    self.show_lines()

  def show_lines(self):
    # vertical lines
    pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(SQSIZE*2,0),(SQSIZE*2,HEIGHT),LINE_WIDTH)
    # horizontal lines
    pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE*2),(WIDTH,SQSIZE*2),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
  
  def next_turn(self):
    self.player = self.player %2+1
    
  def draw_fig(self,row,col):
    if self.player==1:
      # draw x
      # desc line
      start_desc = (col*SQSIZE + OFFSET, row*SQSIZE+OFFSET)
      end_desc = (col*SQSIZE+SQSIZE - OFFSET, row*SQSIZE+SQSIZE-OFFSET)
      #asc line
      start_asc = (col*SQSIZE + OFFSET, row*SQSIZE+SQSIZE-OFFSET)
      end_asc = (col*SQSIZE+SQSIZE - OFFSET, row*SQSIZE+OFFSET)
      pygame.draw.line(screen,LINE_COLOR,start_desc,end_desc,LINE_WIDTH)
      pygame.draw.line(screen,LINE_COLOR,start_asc,end_asc,LINE_WIDTH)
      
    elif self.player==2:
      # draw 0
      center = (col * SQSIZE + SQSIZE//2, row*SQSIZE + SQSIZE//2)
      pygame.draw.circle(screen,PLAYER_COLOR,center,RADIUS,LINE_WIDTH)
    
def main():
  # creating the game object
  game = Game()
  board = game.board
  
  # main loop
  while True:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = event.pos
        row = pos[1]//SQSIZE
        col = pos[0]//SQSIZE
        if board.empty_sqr(row,col):
          board.mark_sqr(row,col,game.player)
          game.draw_fig(row,col)
          game.next_turn()
        print(board.squares)
      
    pygame.display.update()
main()