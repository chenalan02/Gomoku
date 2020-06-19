import pygame

##
#subprogram to draw the board
def drawBoard(screen, light_orange, black):
    
    screen.fill(light_orange)

    #draws vertical lines
    for i in range(0, 595, 35):
        pygame.draw.line(screen, black, [i, 0],[i, 595],2 )

    #draws horizontal lines
    for i in range(0, 595, 35):
        pygame.draw.line(screen, black, [0, i],[595, i],2 )

    #draws border
    pygame.draw.rect(screen, black, [0, 0, 595, 595], 30)
    
##
#function to display who won
#parameter winner
def drawWinScreen(screen, winner, black):
    
    font= pygame.font.SysFont('Calibri', 30, True, False)
    text= font.render(winner+" wins", True, black)
    screen.blit(text, [230,260])

##
#function for placement error
def drawPlacementError(screen, black):
    font= pygame.font.SysFont('Calibri', 30, True, False)
    text= font.render("There is already a chip here!", True, black)
    screen.blit(text, [120,20])

##
#functions for drawing restart option
def drawRestartOption(screen, black, white):
    font= pygame.font.SysFont('Calibri', 30, True, False)
    text= font.render("Would you like to play again?", True, black)
    screen.blit(text, [120,20])

    #draw yes and no buttons
    pygame.draw.rect(screen, black, [35,250,200,100])
    pygame.draw.rect(screen, black, [360,250,200,100])
    
    font= pygame.font.SysFont('Calibri', 100, True, False)
    text= font.render("Yes", True, white)
    screen.blit(text, [60,255])
    text= font.render("No", True, white)
    screen.blit(text, [400,255])