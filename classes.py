import pygame , sys
import time
import os
clock = pygame.time.Clock()

class grid():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Bsize = 50
        self.color = (0,244,0)
        #TFgrid = []
        #for i in range(10):
            #TFGrid.append([0 for j in range(10)])
        row0 = []
        for x in range(10):
            row0.append(0)
        row1 = []
        for x in range(10):
            row1.append(0)
        row2 = []
        for x in range(10):
            row2.append(0)
        row3 = []
        for x in range(10):
            row3.append(0)
        row4 = []
        for x in range(10):
            row4.append(0)
        row5 = []
        for x in range(10):
            row5.append(0)
        row6 = []
        for x in range(10):
            row6.append(0)
        row7 = []
        for x in range(10):
            row7.append(0)
        row8 = []
        for x in range(10):
            row8.append(0)
        row9 = []
        for x in range(10):
            row9.append(0)
        self.TFgrid = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9]
        self.curs = 5
    def drawGrid(self, win,voltz,Grid):
        h_grid = 10
        w_grid = 10
        for y in range(h_grid):
            for x in range(w_grid):
                self.guide(x,y,win,voltz,Grid)

    def drawSqr(self,win):
        rect = pygame.Rect(self.x * (self.Bsize + 1), self.y * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, self.color, rect)
        self.NOToccupy(self.x, self.y)

    def CURSimage(self,win,sprite,inX,inY):
        sprite = pygame.sprite.Sprite()  # create sprite
        sprite.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\Cccursor.png").convert_alpha()
        sprite.rect = sprite.image.get_rect()  # use image extent values
        sprite.rect = [inX * (50 + 1), inY * (50 + 1)]  # put the ball in the top left corner
        win.blit(sprite.image, sprite.rect)
        #pygame.display.update()

    def moveCursor(self):
        self.curs = 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x < 9:
            self.x += 1

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 1

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 1

        if keys[pygame.K_DOWN] and self.y < 9:
            self.y += 1

    def drawCursor(self,win,voltz):
        pic = "C:\\Users\\HP Owner\\Downloads\\Cccursor.png"
        self.CURSimage(win,pic,self.x,self.y)

    def occupy(self, inputX, inputY, input):
        self.TFgrid[inputY][inputX] = input

    def NOToccupy(self, inputX, inputY):
        self.TFgrid[inputY][inputX] = 0

    def IsOccupied(self, inputX, inputY):
        return self.TFgrid[inputY][inputX]

    def guide(self, inX, inY, win,voltz, Grid):
        # 0 - blank tile, 1 - uptile, 2 - sidetile, 3 - startsqr, 4 - endsqr
        if self.TFgrid[inY][inX] == 0:
            rect = pygame.Rect(inX * (self.Bsize + 1), inY * (self.Bsize + 1), self.Bsize, self.Bsize)
            pygame.draw.rect(win, self.color, rect)
        elif self.TFgrid[inY][inX] == 1:
            voltz.SIDEwire(win,inX,inY,Grid)
        elif self.TFgrid[inY][inX] == 2:
            voltz.UPwire(win,inX,inY,Grid)
        elif self.TFgrid[inY][inX] == 3:
            voltz.startSqr(win,Grid)
        elif self.TFgrid[inY][inX] == 4:
            voltz.endSqr(win,Grid)

    def menu(self, win, voltz, Grid):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            voltz.UPwire(win, self.x, self.y, Grid)

        if keys[pygame.K_s]:
            voltz.SIDEwire(win, self.x, self.y, Grid)

        if keys[pygame.K_r]:
            self.drawSqr(win)
        if keys[pygame.K_e]:
            voltz.Path(Grid)


    def drawMenu(self, win,voltz, Grid):
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        MENU = pygame.Rect(515, 5, 190, 500)
        pygame.draw.rect(win, (244, 0, 0), MENU)
        text3 = "Menu"
        textsurf2 = Font.render(text3, False, (0, 0, 0))
        win.blit(textsurf2, (570, 10))

        button = pygame.Rect(540, 200, 70, 50)
        pygame.draw.rect(win, (244, 244, 0), button)
        text2 = "Wire"
        textsurf = Font.render(text2, False, (0, 0, 0))
        win.blit(textsurf, (545, 200))

        button2 = pygame.Rect(540, 300, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button2)
        text3 = "Battery"
        textsurf = Font.render(text3, False, (0, 0, 0))
        win.blit(textsurf, (545, 300))

        button3 = pygame.Rect(540, 400, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button3)
        text4 = "Resistor"
        textsurf = Font.render(text4, False, (0, 0, 0))
        win.blit(textsurf, (545, 400))

        mouse = pygame.mouse.get_pos()
        m1, m2, m3 = pygame.mouse.get_pressed()
        #print(mouse)
        if 540+70 > mouse[0] > 540 and 200 + 50 > mouse[1] > 200 and m1 == True:
            voltz.UPwire(win, self.x, self.y, Grid)

        if 540+130 > mouse[0] > 540 and 300 + 50 > mouse[1] > 300 and m1 == True:
            voltz.v1 = voltz.v1 + 2

        if 540+130 > mouse[0] > 540 and 400 + 50 > mouse[1] > 400 and m1 == True:
            voltz.v1 = voltz.v1 - 1


class Voltage():
    def __init__(self):
        self.v1 = 5
        self.v2 = 10
        self.xB = 0
        self.yB = 0
        self.xE = 6
        self.yE = 7
        self.Bsize = 50
        b = pygame.sprite.Sprite()  # create sprite
        b.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\SidePipe.png").convert_alpha()
        self.Spipe = b
        a = pygame.sprite.Sprite()  # create sprite
        a.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\SidePipe.png").convert_alpha()
        self.Upipe = a

    def startSqr(self,win,Grid):
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(self.xB * (self.Bsize + 1), self.yB * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, (139, 136, 120), rect)
        Grid.occupy(self.xB, self.yB,3)
        txtV1 = str(self.v1)
        textsurf2 = Font.render(txtV1, False, (0, 0, 0))
        win.blit(textsurf2, (self.xB * (self.Bsize + 1) + 10, self.yB * (self.Bsize + 1) + 5))

    def endSqr(self,win,Grid):

        Font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(self.xE * (self.Bsize + 1), self.yE * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, (139, 136, 120), rect)
        Grid.occupy(self.xE, self.yE,4)
        txtV2 = str(self.v2)
        textsurf2 = Font.render(txtV2, False, (0, 0, 0))
        win.blit(textsurf2, (self.xE * (self.Bsize + 1) + 10, self.yE * (self.Bsize + 1) + 5))

    def UPwire(self,win,inX,inY,Grid):
        if(Grid.IsOccupied(inX,inY) == 0 or Grid.IsOccupied(inX, inY) == 2):
            self.curs = 0
            pic = "C:\\Users\\HP Owner\\Downloads\\Pipe2.png"
            #Grid.drawSqr(win)
            self.PICimage(win,self.Upipe,inX,inY)
            Grid.occupy(inX, inY,2)

    def SIDEwire(self,win,inX,inY,Grid):
        if (Grid.IsOccupied(inX, inY) == 0 or Grid.IsOccupied(inX, inY) == 1):
            self.curs = 0
            #print(os.getcwd())
            pic = "C:\\Users\\HP Owner\\Downloads\\SidePipe.png"
            #Grid.drawSqr(win)
            self.PICimage(win,self.Spipe,inX,inY)
            Grid.occupy(inX, inY,1)

    def PICimage(self,win,sprite,inX,inY):
        sprite.rect = sprite.image.get_rect()  # use image extent values
        sprite.rect = [inX * (50 + 1), inY * (50 + 1)]  # put the ball in the top left corner
        win.blit(sprite.image, sprite.rect)
        #pygame.display.update()

    def winCon(self,Grid):
        return self.v1 == self.v2 and self.Path(Grid)

    def Path(self,Grid):
        a = self.xB
        b = self.yB
        count = 0
        while a != self.xE and b != self.yE:
            repeat = False
            if Grid.IsOccupied(a+1, b) > 0 and repeat == False:
                a = a+1
                repeat = True
            elif Grid.IsOccupied(a, b+1) > 0 and repeat == False:
                b = b+1
                repeat = True
            elif Grid.IsOccupied(a, b-1) > 0 and repeat == False:
                b = b-1
                repeat = True
            elif Grid.IsOccupied(a-1, b) > 0 and repeat == False:
                a = a-1
                repeat = True
            elif count == 25:
                break
            else:
                count+=1


        return True
''' 
win condition
battery and resistors
fix grid
clean up code
sprite work -> piskel character tutorial
'''















