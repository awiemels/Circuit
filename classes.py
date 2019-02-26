import pygame

class grid():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Bsize = 50
        self.color = (0,244,0)

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


    def moveCursor(self):
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
        TopRect = pygame.Rect(self.x * (self.Bsize + 1), self.y * (self.Bsize + 1), self.Bsize, 2)
        LeftRect= pygame.Rect(self.x * (self.Bsize + 1), self.y * (self.Bsize + 1), 2, self.Bsize)
        BottomRect = pygame.Rect(self.x * (self.Bsize + 1), self.y * (self.Bsize + 1)+(self.Bsize-2), self.Bsize, 2)
        RightRect = pygame.Rect(self.x * (self.Bsize + 1)+(self.Bsize-2), self.y * (self.Bsize + 1), 2, self.Bsize)

        self.moveCursor()
        pygame.draw.rect(win, (244, 0, 0), TopRect)
        pygame.draw.rect(win, (244, 0, 0), LeftRect)
        pygame.draw.rect(win, (244, 0, 0), BottomRect)
        pygame.draw.rect(win, (244, 0, 0), RightRect)

    def occupy(self, inputX, inputY):
        self.TFgrid[inputY][inputX] = 1

    def NOToccupy(self, inputX, inputY):
        self.TFgrid[inputY][inputX] = 0

    def IsOccupied(self, inputX, inputY):
        return self.TFgrid[inputY][inputX]

    def IsNotOccupied(self, inputX, inputY):
        return not self.TFgrid[inputY][inputX]

    def menu(self, win,voltz,Grid):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            voltz.UPwire(win,self.x,self.y,Grid)
        if keys[pygame.K_s]:
            voltz.SIDEwire(win,self.x, self.y,Grid)
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
            rect = pygame.Rect(inX * (self.Bsize + 1), inY * (self.Bsize + 1) + (.25) * self.Bsize, self.Bsize, (.5) * self.Bsize)
            pygame.draw.rect(win, (244, 0, 0), rect)
            Grid.occupy(inX, inY)


    def SIDEwire(self,win,inX,inY,Grid):
        if (Grid.IsNotOccupied(inX, inY)):
            rect = pygame.Rect(inX * (self.Bsize + 1)+(.25) * self.Bsize, inY * (self.Bsize + 1), (.5) * self.Bsize,self.Bsize)
            pygame.draw.rect(win, (244, 0, 0), rect)
            Grid.occupy(inX, inY)







