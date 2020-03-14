import pygame
from grid import Grid
pygame.init()
grid=Grid()
grid.display(0,0)
screen=pygame.display.set_mode((600,600))

pygame.display.set_caption("Ultimate Tic Tac Toe")

icon=pygame.image.load("C:\\Users\\Home\\Desktop\\Python\\Game1\\tic-tac-toe.png")
pygame.display.set_icon(icon)
x=pygame.image.load("C:\\Users\\Home\\Desktop\\Python\\Game1\\x-png-35397.png")

o=pygame.image.load("C:\\Users\\Home\\Desktop\\Python\\Game1\\circle-png-25312.png")

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                flag=grid.mark(pos[0],pos[1],screen)
                grid.count=grid.count+1
                if flag!=(-1,-1):
                    if grid.count%2==1:
                        screen.blit(o,flag)
                    else:
                        screen.blit(x,flag)
    if grid.gameover=='':
        grid.draw(screen)
    elif grid.gameover=='X':
        x=pygame.image.load("C:\\Users\\Home\\Desktop\\Python\\Game1\\owin.png")    
        screen.blit(x,(0,200))
    else:
        x=pygame.image.load("C:\\Users\\Home\\Desktop\\Python\\Game1\\o-win.png")    
        screen.blit(x,(0,200))
    pygame.display.update()