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
        self.TFgrid = []
        for i in range(10):
            self.TFgrid.append([0 for j in range(10)])
        self.run = True

        self.v1 = 5
        self.v2 = 10
        self.xB = 0
        self.yB = 0
        self.xE = 6
        self.yE = 7
        b = pygame.sprite.Sprite()  # create sprite
        b.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\SidePipe.png").convert_alpha()
        self.Spipe = b
        a = pygame.sprite.Sprite()  # create sprite
        a.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\SidePipe.png").convert_alpha()
        self.Upipe = a
        c = pygame.sprite.Sprite()  # create sprite
        c.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\battery.png").convert_alpha()
        self.battery = c
        d = pygame.sprite.Sprite()  # create sprite
        d.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\resistor.png").convert_alpha()
        self.resistor = d

    def drawResistor(self, win, inX, inY):
        if (self.IsOccupied(inX, inY) == 0 or self.IsOccupied(inX, inY) == 5):
            self.PICimage(win,self.resistor, inX, inY)
            if self.IsOccupied(inX, inY) == 0:
                self.v1 = self.v1 - 1
            self.occupy(inX, inY,5)

    def drawBattery(self, win, inX, inY):
        if (self.IsOccupied(inX, inY) == 0 or self.IsOccupied(inX, inY) == 6):
            self.PICimage(win,self.battery, inX, inY)
            if self.IsOccupied(inX, inY) == 0:
                self.v1 = self.v1 + 2
            self.occupy(inX, inY,6)

    def drawGrid(self, win):
        h_grid = 10
        w_grid = 10
        for y in range(h_grid):
            for x in range(w_grid):
                self.guide(x,y,win)

    def drawSqr(self,win):
        rect = pygame.Rect(self.x * (self.Bsize + 1), self.y * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, self.color, rect)
        if self.IsOccupied(self.x,self.y) == 5:
            self.v1 = self.v1 + 1
        elif self.IsOccupied(self.x,self.y) == 6:
            self.v1 = self.v1 - 2
        self.NOToccupy(self.x, self.y)

    def CURSimage(self,win,sprite,inX,inY):
        sprite = pygame.sprite.Sprite()  # create sprite
        sprite.image = pygame.image.load("C:\\Users\\HP Owner\\Downloads\\Cccursor.png").convert_alpha()
        sprite.rect = sprite.image.get_rect()  # use image extent values
        sprite.rect = [inX * (50 + 1), inY * (50 + 1)]  # put the ball in the top left corner
        win.blit(sprite.image, sprite.rect)


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

    def drawCursor(self,win):
        pic = "C:\\Users\\HP Owner\\Downloads\\Cccursor.png"
        self.CURSimage(win,pic,self.x,self.y)

    def occupy(self, inputX, inputY, input):
        self.TFgrid[inputY][inputX] = input

    def NOToccupy(self, inputX, inputY):
        self.TFgrid[inputY][inputX] = 0

    def IsOccupied(self, inputX, inputY):
        return self.TFgrid[inputY][inputX]

    def guide(self, inX, inY, win):
        # 0 - blank tile, 1 - uptile, 2 - sidetile, 3 - startsqr, 4 - endsqr 5 - resistor, 6 - battery
        if self.TFgrid[inY][inX] == 0:
            rect = pygame.Rect(inX * (self.Bsize + 1), inY * (self.Bsize + 1), self.Bsize, self.Bsize)
            pygame.draw.rect(win, self.color, rect)
        elif self.TFgrid[inY][inX] == 1:
            self.SIDEwire(win,inX,inY)
        elif self.TFgrid[inY][inX] == 2:
            self.UPwire(win,inX,inY)
        elif self.TFgrid[inY][inX] == 3:
            self.startSqr(win)
        elif self.TFgrid[inY][inX] == 4:
            self.endSqr(win)
        elif self.TFgrid[inY][inX] == 5:
            self.drawResistor(win,inX, inY)
        elif self.TFgrid[inY][inX] == 6:
            self.drawBattery(win,inX, inY)



    def menu(self, win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            self.UPwire(win, self.x, self.y)

        if keys[pygame.K_s]:
            self.SIDEwire(win, self.x, self.y)

        if keys[pygame.K_r]:
            self.drawSqr(win)
        if keys[pygame.K_e]:
            self.Path()


    def drawMenu(self, win):
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        MENU = pygame.Rect(515, 5, 190, 500)
        pygame.draw.rect(win, (244, 0, 0), MENU)
        text3 = "Menu"
        textsurf2 = Font.render(text3, False, (0, 0, 0))
        win.blit(textsurf2, (570, 10))

        button = pygame.Rect(540, 55, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button)
        text2 = "Wire"
        textsurf = Font.render(text2, False, (0, 0, 0))
        win.blit(textsurf, (545, 55))

        button2 = pygame.Rect(540, 155, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button2)
        text3 = "Battery"
        textsurf = Font.render(text3, False, (0, 0, 0))
        win.blit(textsurf, (545, 155))

        button3 = pygame.Rect(540, 255, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button3)
        text4 = "Resistor"
        textsurf = Font.render(text4, False, (0, 0, 0))
        win.blit(textsurf, (545, 255))

        button4 = pygame.Rect(540, 355, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button4)
        text4 = "Power"
        textsurf = Font.render(text4, False, (0, 0, 0))
        win.blit(textsurf, (545, 355))

        button5 = pygame.Rect(540, 425, 130, 50)
        pygame.draw.rect(win, (244, 244, 0), button5)
        text4 = "undo"
        textsurf = Font.render(text4, False, (0, 0, 0))
        win.blit(textsurf, (545, 425))

        mouse = pygame.mouse.get_pos()
        m1, m2, m3 = pygame.mouse.get_pressed()

        if 540+130 > mouse[0] > 540 and 55 + 50 > mouse[1] > 55 and m1 == True:
            self.UPwire(win, self.x, self.y)

        if 540+130 > mouse[0] > 540 and 155 + 50 > mouse[1] > 155 and m1 == True:
            self.drawBattery(win, self.x, self.y)

        if 540+130 > mouse[0] > 540 and 255 + 50 > mouse[1] > 255 and m1 == True:
            self.drawResistor(win, self.x,self.y)

        if 540+130 > mouse[0] > 540 and 425 + 50 > mouse[1] > 425 and m1 == True:
            self.drawSqr(win)

        if 540+130 > mouse[0] > 540 and 355 + 50 > mouse[1] > 355 and m1 == True:
            if self.winCon() == True:
                print("Thank you for playing")
                self.run = False


    def startSqr(self,win):
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(self.xB * (self.Bsize + 1), self.yB * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, (139, 136, 120), rect)
        self.occupy(self.xB, self.yB,3)
        txtV1 = str(self.v1)
        textsurf2 = Font.render(txtV1, False, (0, 0, 0))
        win.blit(textsurf2, (self.xB * (self.Bsize + 1) + 10, self.yB * (self.Bsize + 1) + 5))

    def endSqr(self,win):
        Font = pygame.font.SysFont('Comic Sans MS', 30)
        rect = pygame.Rect(self.xE * (self.Bsize + 1), self.yE * (self.Bsize + 1), self.Bsize, self.Bsize)
        pygame.draw.rect(win, (139, 136, 120), rect)
        self.occupy(self.xE, self.yE,4)
        txtV2 = str(self.v2)
        textsurf2 = Font.render(txtV2, False, (0, 0, 0))
        win.blit(textsurf2, (self.xE * (self.Bsize + 1) + 10, self.yE * (self.Bsize + 1) + 5))

    def UPwire(self,win,inX,inY):
        if(self.IsOccupied(inX,inY) == 0 or self.IsOccupied(inX, inY) == 2):
            self.PICimage(win,self.Upipe,inX,inY)
            self.occupy(inX, inY,2)

    def SIDEwire(self,win,inX,inY):
        if (self.IsOccupied(inX, inY) == 0 or self.IsOccupied(inX, inY) == 1):
            self.PICimage(win,self.Spipe,inX,inY)
            self.occupy(inX, inY,1)

    def PICimage(self,win,sprite,inX,inY):
        sprite.rect = sprite.image.get_rect()  # use image extent values
        sprite.rect = [inX * (50 + 1), inY * (50 + 1)]  # put the ball in the top left corner
        win.blit(sprite.image, sprite.rect)


    def winCon(self):
        return self.v1 == self.v2 and self.Path()

    def Path(self):
        a = self.xB
        b = self.yB
        count = 0
        while a != self.xE and b != self.yE:
            if self.IsOccupied(a+1, b) > 0:
                a = a+1
            elif self.IsOccupied(a, b+1) > 0:
                b = b+1
            elif self.IsOccupied(a, b-1) > 0:
                b = b-1
            elif self.IsOccupied(a-1, b) > 0:
                a = a-1
            elif count == 25:
                return False
            else:
                count+=1
        return True

class draw():
    def __init__(self):
        self.pic = 5

    def math(self):
        return self.pic +5


''' 
Multiple Levels
WIn message
Fix wire Drawing
    Automatic fixing tiling up down turn tiles
    Limits on placing wires/Batteries/Resistors
DFS algorithm 
sprite work -> piskel character tutorial
'''















