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
        self.A = True

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
    def drawGrid(self, win):
        h_grid = 10
        w_grid = 10
        for y in range(h_grid):
            for x in range(w_grid):
                if(self.IsNotOccupied(x,y)):
                    rect = pygame.Rect(x * (self.Bsize + 1), y * (self.Bsize + 1), self.Bsize, self.Bsize)
                    pygame.draw.rect(win, self.color, rect)

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
        if (self.IsNotOccupied(self.x, self.y) or self.curs == 5):
            pic = "C:\\Users\\HP Owner\\Downloads\\Cccursor.png"
            self.CURSimage(win,pic,self.x,self.y)

    def occupy(self, inputX, inputY):
        self.TFgrid[inputY][inputX] = 1

    def NOToccupy(self, inputX, inputY):
        self.TFgrid[inputY][inputX] = 0

    def IsOccupied(self, inputX, inputY):
        return self.TFgrid[inputY][inputX]

    def IsNotOccupied(self, inputX, inputY):
        return not self.TFgrid[inputY][inputX]




    def guide(self, inX, inY, win,voltz, Grid):
        # 0 - blank tile, 1 - uptile, 2 - sidetile, 3 - startsqr, 4 - endsqr
        if self.TFgrid[inY][inX] == 0:
            rect = pygame.Rect(inX * (self.Bsize + 1), inY * (self.Bsize + 1), self.Bsize, self.Bsize)
            pygame.draw.rect(win, self.color, rect)
        elif self.TFgrid[inY][inX] == 1:
            rect = pygame.Rect(inX * (self.Bsize + 1), inY * (self.Bsize + 1), self.Bsize, self.Bsize)
            pygame.draw.rect(win, self.color, rect)
            voltz.SIDEwire(win,inX,inY,Grid)
        elif self.TFgrid[inY][inX] == 2:
            rect = pygame.Rect(inX * (self.Bsize + 1), inY * (self.Bsize + 1), self.Bsize, self.Bsize)
            pygame.draw.rect(win, self.color, rect)
            voltz.UPwire(win,inX,inY,Grid)
        elif self.TFgrid[inY][inX] == 3:
            voltz.startSqr(win,Grid)
        elif self.TFgrid[inY][inX] == 4:
            voltz.endSqr(win,Grid)




    def menu(self, win, voltz, Grid):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            self.A = False
            voltz.UPwire(win, self.x, self.y, Grid)
            self.A = True
        if keys[pygame.K_s]:
            self.A = False
            voltz.SIDEwire(win, self.x, self.y, Grid)
            self.A = True
        if keys[pygame.K_r]:
            self.drawSqr(win)


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
        b.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\Pipe.png").convert_alpha()
        self.Spipe = b
        a = pygame.sprite.Sprite()  # create sprite
        a.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\Pipe.png").convert_alpha()
        self.Upipe = a

    def startSqr(self,win,Grid):
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(self.xB * (self.Bsize + 1), self.yB * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, (139, 136, 120), rect)
        Grid.occupy(self.xB, self.yB)
        txtV1 = str(self.v1)
        textsurf2 = Font.render(txtV1, False, (0, 0, 0))
        win.blit(textsurf2, (self.xB * (self.Bsize + 1) + 10, self.yB * (self.Bsize + 1) + 5))

    def endSqr(self,win,Grid):

        Font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(self.xE * (self.Bsize + 1), self.yE * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, (139, 136, 120), rect)
        Grid.occupy(self.xE, self.yE)
        txtV2 = str(self.v2)
        textsurf2 = Font.render(txtV2, False, (0, 0, 0))
        win.blit(textsurf2, (self.xE * (self.Bsize + 1) + 10, self.yE * (self.Bsize + 1) + 5))

    def UPwire(self,win,inX,inY,Grid):
        if(Grid.IsNotOccupied(inX,inY)):
            self.curs = 0
            pic = "C:\\Users\\HP Owner\\Downloads\\Pipe2.png"
            Grid.drawSqr(win)
            self.PICimage(win,self.Upipe,inX,inY)
            Grid.occupy(inX, inY)

            


    def SIDEwire(self,win,inX,inY,Grid):
        if (Grid.IsNotOccupied(inX, inY)):
            self.curs = 0
            #print(os.getcwd())
            pic = "C:\\Users\\HP Owner\\Downloads\\Pipe.png"
            Grid.drawSqr(win)
            self.PICimage(win,self.Spipe,inX,inY)
            Grid.occupy(inX, inY)



    def PICimage(self,win,sprite,inX,inY):

        sprite.rect = sprite.image.get_rect()  # use image extent values
        sprite.rect = [inX * (50 + 1), inY * (50 + 1)]  # put the ball in the top left corner
        win.blit(sprite.image, sprite.rect)
        #pygame.display.update()












