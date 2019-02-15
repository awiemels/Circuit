import pygame


pygame.init()
pygame.font.init()
win = pygame.display.set_mode((500,500))
pygame.display.flip()


def grid():
  h_grid = 10
  w_grid = 10
  block_size = 50
  color = (0, 244, 0)
  for y in range(h_grid):
    for x in range(w_grid):
      rect = pygame.Rect(x * (block_size + 1), y * (block_size + 1), block_size, block_size)
      pygame.draw.rect(win, color, rect)

class Voltage():
  def __init__(self, x, y, v1, v2):
    self.x = x
    self.y = y
    self. v1 = v1
    self.v2 = v2

  def startSqr(self):
    block_size = 50
    Font = pygame.font.SysFont('Comic Sans MS', 30)
    rect = pygame.Rect(0*(block_size + 1), 0*(block_size + 1), block_size, block_size)
    pygame.draw.rect(win, (139,136,120), rect)
    txtV1 = str(self.v1)
    textsurf2 = Font.render(txtV1, False, (0, 0, 0))
    win.blit(textsurf2, (15, 5))

  def endSqr(self):
    block_size = 50
    Font = pygame.font.SysFont('Comic Sans MS', 30)
    rect = pygame.Rect(self.x * (block_size+1), self.y * (block_size+1), block_size, block_size)
    pygame.draw.rect(win, (139,136,120), rect)
    txtV2 = str(self.v2)
    textsurf2 = Font.render(txtV2, False, (0, 0, 0))
    win.blit(textsurf2, (self.x *(block_size+1)+10, self.y *(block_size+1)+5))



class wire():
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.side = True
  def draw(self):
    block_size = 50
    self.move()
    rect = pygame.Rect(self.x * (block_size + 1), self.y * (block_size + 1)+(1/4)*block_size, block_size, (1 / 2) * block_size)
    rect2 = pygame.Rect(self.x * (block_size + 1)+(1/4)*block_size, self.y * (block_size + 1), (1 / 2) * block_size, block_size)
    if self.x == 0 and self.y == 0:
      state = True
    else:
      state = False
    if self.side == True and state == False:
      pygame.draw.rect(win, (244, 0, 0), rect)
    if self.side == False and state == False:
      pygame.draw.rect(win, (244, 0, 0), rect2)

  def move(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and self.x < 9:
      self.x += 1
      self.side = True

    if keys[pygame.K_LEFT] and self.x > 0:
      self.x -= 1
      self.side = True

    if keys[pygame.K_UP] and self.y > 0:
      self.y -= 1
      self.side = False

    if keys[pygame.K_DOWN] and self.y < 9:
      self.y += 1
      self.side = False



circuit = wire(0,0)
volt = Voltage(6,5,5,25)

def redraw():

  grid()
  circuit.draw()
  volt.endSqr()
  volt.startSqr()
  pygame.display.update()
  pygame.time.delay(70)

def playGame():
  win.fill((0,0,0))
  running = True
  while running:
    for event in pygame.event.get():
      # print(event)
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        quit()

    redraw()


def game_intro():
  choice = True
  while choice:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    Font = pygame.font.SysFont('Comic Sans MS', 30)
    text = "welcome to circuit game"
    textsurface = Font.render(text, False, (255, 0, 0))
    win.blit(textsurface, (100, 50))
    pygame.display.update()

    button = pygame.Rect(150, 200, 150, 50)
    pygame.draw.rect(win, (244, 0, 0), button)
    text2 = "play"
    textsurf = Font.render(text2, False, (0, 0, 0))
    win.blit(textsurf, (200, 200))
    #pygame.display.update()

    button2 = pygame.Rect(150, 300, 150, 50)
    pygame.draw.rect(win, (244, 0, 0), button2)
    text3 = "quit"
    textsurf2 = Font.render(text3, False, (0, 0, 0))
    win.blit(textsurf2, (200, 300))
    #pygame.display.update()


    mouse = pygame.mouse.get_pos()
    m1, m2, m3 = pygame.mouse.get_pressed()
    if 150 + 150 > mouse[0] > 150 and 200 + 50 > mouse[1] > 200:
      pygame.draw.rect(win, (0, 200, 0), button)
      textsurf = Font.render(text2, False, (0, 0, 0))
      win.blit(textsurf, (200, 200))
    if 150 + 150 > mouse[0] > 150 and 200 + 50 > mouse[1] > 200 and m1 == True:
      choice = False
    if 150 + 150 > mouse[0] > 150 and 300 + 50 > mouse[1] > 300:
      pygame.draw.rect(win, (0, 200, 0), button2)
      textsurf = Font.render(text3, False, (0, 0, 0))
      win.blit(textsurf2, (200, 300))
    if 150 + 150 > mouse[0] > 150 and 300 + 50 > mouse[1] > 300 and m1 == True:
      quit()

def main():
  game_intro()
  playGame()


main()













