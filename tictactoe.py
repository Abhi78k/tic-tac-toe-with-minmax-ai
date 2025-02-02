import sys
import pygame
import numpy as np
import random
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("This is my tic tac toe AI")
screen.fill(BG_COLOR)

class Board:
  def __init__(self):
    self.squares = np.zeros((ROWS,COLUMNS))
    self.empty_sqrs = self.squares #[squares]
    self.marked_sqrs=0
  
  def final_state(self):
    '''
      return 0 if there is no win yet (we will be checking for draws only using the isfull function)
      return 1 if player 1 has won
      return 2 if player 2 has won
    '''
    #vertical wins
    for col in range(COLUMNS):
      if self.squares[0][col]==self.squares[1][col]==self.squares[2][col]!=0:
        return self.squares[0][col]
    
    # horizontal wins 
    for row in range(ROWS):
      if self.squares[0][row]==self.squares[1][row]==self.squares[2][row]!=0:
        return self.squares[0][row]
    
    #desc diagonal
    if self.squares[0][0] == self.squares[1][1] == self.squares [2][2]!=0:
      return self.squares[0][0]
    
    # ascending diagonal
    if self.squares[2][0] == self.squares[1][1] == self.squares [0][2]!=0:
      return self.squares[0][0]
    
    # return 0 if there is no win yet
    return 0
  def mark_sqr(self,row,col,player):
    self.squares[row][col]=player
    self.marked_sqrs+=1

  def empty_sqr(self,row,col):
    return self.squares[row][col]==0
  
  def get_empty_sqrs(self):
    empty_sqrs=[]
    for row in range(ROWS):
      for col in range(COLUMNS):
        if self.empty_sqr(row,col):
          empty_sqrs.append((row,col))
    return empty_sqrs
  
  def isfull(self):
    return self.marked_sqrs==9
  
  def isempty(self):
    return self.marked_sqrs==0
  
class AI:
  def __init__(self,level=0,player=2):
    self.level = level
    self.player=player
  
  def rnd(self,board):
    empty_sqrs = board.get_empty_sqrs()
    idx = random.randrange(0,len(empty_sqrs))
    return empty_sqrs[idx] #returning (row,col)
  
  def eveal(self,main_board):
    if self.level==0:
      # random choice
      move = self.rnd(main_board)
    else:
      # minimax algo choice
      pass
      return move #(row,col)

class Game:
  def __init__(self):
    self.board = Board()
    self.ai = AI()
    self.player = 1
    self.gamemode = 'pvp' #pvp or ai
    self.running = True
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
  ai = game.ai
  
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
    
    if game.gamemode=='ai' and game.player == ai.player:
      pygame.display.update()
      # ai methods
      row,col = ai.eval(board)
      board.mark_sqr(row,col,game.player)
      game.draw_fig(row,col)
      game.next_turn()
      
    pygame.display.update()
main()