import pygame
import time
from classes import grid, Voltage

pygame.init()
pygame.font.init()
win = pygame.display.set_mode((710,510))
pygame.display.flip()
# 510, 510
voltz = Voltage()
Grid = grid()


def redraw():
    Grid.drawGrid(win,voltz,Grid)
    Grid.drawCursor(win,voltz)
    pygame.display.update()
    voltz.startSqr(win, Grid)
    voltz.endSqr(win, Grid)
    Grid.menu(win, voltz, Grid)
    Grid.drawMenu(win,voltz,Grid)
    pygame.display.update()


def playGame():
    win.fill((0, 0, 0))
    Grid.drawGrid(win,voltz,Grid)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            else:
                Grid.moveCursor()
                redraw()


def game_intro():
    choice = True
    while choice:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
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


# add else statements to game loop, fix quitting, other general stuff
# make overall grid class that has glowy border cursor
# check out stuff in math game file and other stuff from bible
# document in implementation doc
# tuxemon github
# sprites










