##
# @Description of Problem: Create a activity from your childhood into a videogame
# @Author: Alan Chen
# @Course Code: ICS3U1-03
# @Date: 2018-06-16

import draw
import pygame
pygame.init()

##
#create class for a 16x16 matrix
class Matrix():
    def __init__(self):

        #set win and turn variables
        self.win= False
        self.turn= ""

        #create 16x16 matrix(lists inside list)
        self.matrix= []
        #creates 16 rows
        for row in range(16):
            
            list_columns= []
            #creates 16 columns
            for column in range(16):
                #adds 0 as a placeholder value that means no chips are placed there
                list_columns.append(0)
            #add each row to a list 
            self.matrix.append(list_columns)
            
    ##
    # print  matrix for debugging purposes
    def drawMatrix(self):
        for i in range(16):
            print(self.matrix[i])
        print("")

    ##
    #method/subprogram to play a chip with color as a parameter
    def placeChip(self, color):
        #finds mosue position
        pos= pygame.mouse.get_pos()
        x= pos[0]
        y= pos[1]

        #divides by 35(space between tiles) and rounds to an integer to find the placement in the matrix
        matrix_x=x//35
        matrix_y=y//35

        #multiplies the rounded number and adds 22(as mouse is top left corner of chip) to find its position on the board
        board_x= matrix_x*35+22
        board_y= matrix_y*35+22

        #checks if the spot clicked on is empty or not
        if self.matrix[matrix_y][matrix_x] == 0:
            #places chip in matrix depending on color of turn
            if color == blue:
                self.matrix[matrix_y][matrix_x] = "b"
            else:
                self.matrix[matrix_y][matrix_x] = "o"

            #creates the sprite of the chip and places it on your rounded mouse position
            chip= Chip(color)
            chip.rect.x= board_x
            chip.rect.y= board_y

            all_chips.add(chip)

            #changes turn and hover chip color
            if self.turn== blue:
                self.turn= orange
                hover_chip.changeColor(orange)
            else:
                self.turn= blue
                hover_chip.changeColor(blue)

        #if there is already a chip where you clicked, displays a placement error
        else:
                all_chips.draw(screen)
                draw.drawPlacementError(screen, black)
                pygame.display.flip()
                time.sleep(1.5)

        #checks if a player had won yet
        
        player= self.checkWin("b")
        player= self.checkWin("o")

        #if win is detected, displays the winner for a second and a half
        if self.win== True:
            all_chips.draw(screen)
            if color== blue:
                drawWinScreen(screen, "Blue", black)
            else:
                drawWinScreen(screem, "Orange", black)
            pygame.display.flip()
            time.sleep(1.5)
            win= True

    ##
    #method/subprogram to check if a player has won or not
    #player to be checked as parameter
    def checkWin(self, player):
        #check through rows by checking each individual chip one by one to see if 5 in a row is achieved
        for row in range(16):
            consequtive_chips=0
            for column in range(16):
                #check if index is equal to player, if so add one to consequtive chips
                if self.matrix[row][column] == player:
                    consequtive_chips+= 1
                    #sets win to true if 5 in a row is achieved
                    if consequtive_chips>=5:
                        self.win= True
                else:
                    consequtive_chips= 0
   
        #check down columns by checking each individual chip one by one to see if 5 in a row is achieved  
        for column in range(16):
            consequtive_chips=0
            for row in range(16):
                #check if index is equal to player, if so add one to consequtive chips
                if self.matrix[row][column] == player:
                    consequtive_chips+= 1
                    #sets win to true if 5 in a row is achieved
                    if consequtive_chips>=5:
                        self.win= True
                else:
                    consequtive_chips= 0

        #check diagonals down to the right for top right half
        for rows in range (16):
            consequtive_chips= 0
            row= 0
            column= 0
            for i in range(16):
                try:
                    #check if index is equal to player, if so add one to consequtive chips
                    if self.matrix[rows+row][column] == player:          
                        consequtive_chips+=1
                    #sets win to true if 5 in a row is achieved
                        if consequtive_chips>=5:
                            self.win= True
                    else:
                        consequtive_chips= 0
                except:
                    consequtive_chips= 0
                #adds to both row and column to move down to the right in diagonal each loop
                row+=1
                column+=1
                
        #check diagonals down to the right for bottom left half
        for columns in range (16):
            consequtive_chips= 0
            row= 0
            column= 0
            for i in range(16):
                try:
                    #check if index is equal to player, if so add one to consequtive chips
                    if self.matrix[row][column+columns] == player:
                        consequtive_chips+=1
                        #sets win to true if 5 in a row is achieved
                        if consequtive_chips>=5:
                            self.win= True
                    else:
                        consequtive_chips= 0
                except:
                    consequtive_chips= 0
                #adds to both row and column to move down to the right in diagonal each loop
                row+=1
                column+=1
                
        #check diagonals up to the right for the top left half
        for rows in range(16):
            consequtive_chips= 0
            row= 0
            column= 0
            for i in range(16):
                try:
                    #check if index is equal to player, if so add one to consequtive chips
                    if self.matrix[row+rows][column] == player:
                        consequtive_chips+=1
                        if consequtive_chips>=5:
                            self.win= True
                    else:
                        consequtive_chips= 0
                except:
                    consequtive_chips= 0

                #adds to both row and column to up to the right in diagonal each loop
                row+=-1
                column+=1
                
        #check diagonals up to the right for the bottom right half
        for rows in range(16):
            consequtive_chips= 0
            row= 16
            column= 0
            for i in range(16):
                try:
                    #check if index is equal to player, if so add one to consequtive chips
                    if self.matrix[row+rows][column] == player:
                        consequtive_chips+=1
                        if consequtive_chips>=5:
                            self.win= True
                    else:
                        consequtive_chips= 0
                except:
                    consequtive_chips= 0
                #adds to both row and column to up to the right in diagonal each loop
                row+=-1
                column+=1

        #return the player
        return player

    ##
    #method/subprogram to restart the game
    def restartGame(self):
        #recreates matrix
        self.matrix= []
        for row in range(16):
            list_columns= []
            for column in range(16):
                list_columns.append(0)
                
            self.matrix.append(list_columns)

        #empties all exisiting chips
        all_chips.empty()

        #set win and turn to default values
        self.win= False
        self.turn= orange

        #set mouse to invisible
        pygame.mouse.set_visible(0)

##
#class for chip sprite
class Chip(pygame.sprite.Sprite):
    def __init__(self, color):
        #call all sprite attirbutes and methods
        super().__init__()
        #parameter for color
        self.color= color

        #creates sprite
        self.image= pygame.Surface([28, 28])
        self.image.fill(grey)
        self.image.set_colorkey(grey)
        pygame.draw.circle(self.image, self.color,[14,14], 14)

        #get rect of sprite
        self.rect= self.image.get_rect()

    #method to change the color of the chip
    def changeColor(self, color):
        pygame.draw.circle(self.image, color,[14,14], 14)

if __name__ == "__main__":

    #define colors
    white= (255, 255, 255)
    black= (0, 0, 0)
    light_orange= (247, 193, 101)
    grey= (128,128,128)
    blue= (45, 121, 252)
    orange= (255, 78, 2)

    #set screen
    size = (595, 595)
    screen = pygame.display.set_mode(size)

     #set screen title
    pygame.display.set_caption("Gomoku")

    #define pygame sprite groups
    all_chips= pygame.sprite.Group()
    all_hover_chips= pygame.sprite.Group()

    #creates board
    board= Matrix()

    #sets turn to orange
    board.turn= orange

    #creates a chip to hover around the mouse
    hover_chip= Chip(board.turn)
    all_hover_chips.add(hover_chip)

    #sets mouse to invisible
    pygame.mouse.set_visible(0)

    #sets done to false
    done = False
    #sets clock
    clock = pygame.time.Clock()

    #loops until done
    while not done:
     
        for event in pygame.event.get():
            draw.drawBoard(screen, light_orange, black)
            if event.type == pygame.QUIT: 
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.win != True:
                    try:
                        #try to place a chip if mouse click is detected and win is not true
                        board.placeChip(board.turn)
      
                    except:
                        #passes if chip is placed out of range
                        pass
                    
                else:
                    #if mouse click is detected and someone has won...
                    #gets mouse position
                    pos= pygame.mouse.get_pos()
                    x= pos[0]
                    y= pos[1]

                    #if mouse is on yes button, restart game
                    if x>=35 and x<=235:
                        if y>=250 and y<=350:
                            board.restartGame()

                    #if mouse is on no button, set done to True
                    if x>=360 and x<=560:
                        if y>=250 and y<=350:
                            done= True         

        #if win is true, change hover chip position to mouse position
        if board.win!= True:
            pos= pygame.mouse.get_pos()
            hover_chip.rect.x= pos[0]
            hover_chip.rect.y= pos[1]

        #draws all chips and hover chip
        all_chips.draw(screen)
        all_hover_chips.draw (screen)

        #if win is true, sets mouse to visible and draws restart option
        if board.win== True:
            pygame.mouse.set_visible(1)
            draw.drawRestartOption(screen, black ,white)
        #flips screen
        pygame.display.flip()

        #sets frames per second
        clock.tick(60)

    #if done is true, quits program
    pygame.quit()

