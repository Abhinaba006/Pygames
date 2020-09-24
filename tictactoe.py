# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:55:20 2020

@author: Abhinaba Das
"""


import pygame
import time
import sys
import random
from tkinter import *
from tkinter import messagebox
pygame.init()

# set resolution
d_height = 500
d_width = 500
BOX_SIZE = 120
LINE_WIDTH = 10
#colors
black=(0,0,0)
red =(255,0,0)
green=(0,255,0)
silver=(150,150,150)
random_color=(120,60,190)
white=(255,255,255)

# starting position
x=70
y=80

# rectangles
rec1 = pygame.Rect(x, y,BOX_SIZE, BOX_SIZE)
rec2 = pygame.Rect(x+BOX_SIZE, y,BOX_SIZE, BOX_SIZE)
rec3 = pygame.Rect(x+2*BOX_SIZE, y,BOX_SIZE, BOX_SIZE)
rec4 = pygame.Rect(x, y+BOX_SIZE,BOX_SIZE, BOX_SIZE)
rec5 = pygame.Rect(x+BOX_SIZE, y+BOX_SIZE,BOX_SIZE, BOX_SIZE)
rec6 = pygame.Rect(x+2*BOX_SIZE, y+BOX_SIZE,BOX_SIZE, BOX_SIZE)
rec7 = pygame.Rect(x, y+2*BOX_SIZE,BOX_SIZE, BOX_SIZE)
rec8 = pygame.Rect(x+BOX_SIZE, y+2*BOX_SIZE,BOX_SIZE, BOX_SIZE)
rec9 = pygame.Rect(x+2*BOX_SIZE, y+2*BOX_SIZE,BOX_SIZE, BOX_SIZE)

rectangles = [[rec1, rec2, rec3], [rec4, rec5, rec6], [rec7, rec8, rec9]]


def box(msg):
    Tk().wm_withdraw()
    messagebox.showinfo("CONGRATS!! ", msg)


def drawScore(smallFont, player1score, player2score, tieScore):
    scoreboard = smallFont.render("Player 1: "+str(player1score)+"       "+"Player 2: "+str(player2score)+"      Tie: "+str(tieScore), True, green, black)
    scoreBoardRect = scoreboard.get_rect()
    scoreBoardRect.x = 10
    scoreBoardRect.y = 10
    SCREEN.blit(scoreboard, scoreBoardRect)
    
    
def reset(board, usedBox, player1TurnDone, player1wins, player2wins):
    board = [[False]*3 for _ in range(3)]
    usedBox = [[False]*3 for _ in range(3)]
    player1TurnDown = False
    player1wins = False
    player2wins = False
    return (board, usedBox, player1TurnDone, player1wins, player2wins)

def gameOver(usedBox, board):
    for boxx in range(3):
        for boxy in range(3):
            if usedBox[boxx][boxy]==False:
                return False
    else:
        return True
    
def winCheck(board):
    if ((board[0][0]==board[1][1]==board[2][2]=='X') or       #DIGO
        (board[0][2]==board[1][1]==board[2][0]=='X') or       #DIGO
        (board[0][0]==board[0][1]==board[0][2]=='X') or       #VER
        (board[1][0]==board[1][1]==board[1][2]=='X') or       #VER
        (board[2][0]==board[2][1]==board[2][2]=='X') or       #VER
        (board[0][0]==board[1][0]==board[2][0]=='X') or       #HORI
        (board[0][1]==board[1][1]==board[2][1]=='X') or       #HORI
        (board[0][2]==board[1][2]==board[2][2]=='X')):        #HORI
            player1wins = True
            player2wins = False
            
            return player1wins, player2wins
        
    elif ((board[0][0]==board[1][1]==board[2][2]=='O') or       #DIGO
        (board[2][0]==board[2][1]==board[2][2]=='O') or       #DIGO
        (board[0][0]==board[0][1]==board[0][2]=='O') or       #VER
        (board[1][0]==board[1][1]==board[1][2]=='O') or       #VER
        (board[2][0]==board[2][1]==board[2][2]=='O') or       #VER
        (board[0][0]==board[1][0]==board[2][0]=='O') or       #HORI
        (board[0][1]==board[1][1]==board[2][1]=='O') or       #HORI
        (board[0][2]==board[1][2]==board[2][2]=='O')):        #HORI
            player1wins = False
            player2wins = True
            
            return player1wins, player2wins
    else:
        return False, False
    
def markX(box_x, box_y, markFont):
    mark = markFont.render(" X ", True, red)
    markRect = rectangles[box_x][box_y]
    SCREEN.blit(mark, markRect) #draw one image onto another
def markO(box_x, box_y, markFont):
    mark = markFont.render(" O ", True, green)
    markRect = rectangles[box_x][box_y]
    SCREEN.blit(mark, markRect) #draw one image onto another
    
def getRectAtMousePos(mouse_x, mouse_y):
    for box_x in range(3):
        for box_y in range(3):
            boxRect = rectangles[box_x][box_y]
            if boxRect.collidepoint(mouse_x, mouse_y): #if mouse pointer is in it
                return (box_x, box_y)
    return (None, None)


def drawBoards():
    #ver rect
    pygame.draw.rect(SCREEN, white, pygame.Rect(x+BOX_SIZE, y, LINE_WIDTH, 360))
    pygame.draw.rect(SCREEN, white, pygame.Rect(x+2*BOX_SIZE, y, LINE_WIDTH, 360))    
    
    #hori rect
    pygame.draw.rect(SCREEN, white, pygame.Rect(x, y+BOX_SIZE, 360, LINE_WIDTH-1,))
    pygame.draw.rect(SCREEN, white, pygame.Rect(x, y+2*BOX_SIZE, 360, LINE_WIDTH-1,)) 
    
    
def main():
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((d_height, d_width))
    pygame.init()
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption('Tic Tac Toe')
    SCREEN.fill(black)
    drawBoards()
    
    mouse_x, mouse_y = 0, 0
    
    board = [[False]*3 for _ in range(3)]
    usedBox = [[False]*3 for _ in range(3)]
    
    player1TurnDown = False
    player1wins = False
    player2wins = False
    
    player1score = 0
    player2score = 0
    tieScore = 0


    markFont = pygame.font.SysFont("Helvetica", 110)
    smallFont = pygame.font.Font('freesansbold.ttf', 26)

    while(True):
        for event in pygame.event.get():
            print(board)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouseClicked = True

                
        box_x, box_y = getRectAtMousePos(mouse_x, mouse_y)
        
        if box_x != None and box_y != None:
            if usedBox[box_x][box_y]==False and player1TurnDown == False:
                markX(box_x, box_y, markFont)
                usedBox[box_x][box_y]=True
                board[box_x][box_y]='X'
                player1TurnDown=True
                pygame.display.update()
                
            elif player1TurnDown==True and usedBox[box_x][box_y]==False:
                markO(box_x, box_y, markFont)
                usedBox[box_x][box_y]=True
                board[box_x][box_y]='O'
                player1TurnDown=False
                pygame.display.update()
                
        #chk for victor
        
        player1wins, player2wins = winCheck(board)
        
        if player1wins==True:
            # reset board and message
            player1score += 1
            board, usedBox, player1TurnDown, player1wins, player2wins = reset(board, usedBox, player1TurnDown, player1wins, player2wins)
            box("Plaqyer 1 is the winner! press ENTER to continue.")
            SCREEN.fill(black)
            drawBoards()
        elif player2wins==True:
            # reset board and message
            player2score += 1
            board, usedBox, player1TurnDown, player1wins, player2wins = reset(board, usedBox, player1TurnDown, player1wins, player2wins)
            box("Plaqyer 2 is the winner! press ENTER to continue.")
            SCREEN.fill(black)
            drawBoards()
        else:
            #tie
            if gameOver(usedBox, board):
                board, usedBox, player1TurnDown, player1wins, player2wins = reset(board, usedBox, player1TurnDown, player1wins, player2wins)
                box("It is a tie! press ENTER to continue.")
                SCREEN.fill(black)
                drawBoards()
                
                
        drawScore(smallFont, player1score, player2score, tieScore)
                
        pygame.display.update()
        CLOCK.tick(60)




if __name__=='__main__':
    main()