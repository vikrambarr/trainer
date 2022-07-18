import pygame
from threading import Thread
import time
import requests

pygame.init()
clock = pygame.time.Clock()

winsize = (380, 720)
screen = pygame.display.set_mode(winsize)

border = (100, 100, 100)
unselected = (70, 70, 70)
selected = (50, 50, 50)
hover = (65, 65, 65)

topgap = 5
bottomgap = 150
bordersize = 5
tabsize = ((winsize[0]-(2*bordersize))/6)

mons = ["Zacian-Crowned", "Ditto", "Eternatus", "Pyukumuku", "Blissey", "Sableye-Mega"]




def drawtab(tab):
    screen.fill(border)
    screen.fill(unselected, rect=pygame.Rect(bordersize, topgap, winsize[0]-(2*bordersize), 30))
    screen.fill(selected, rect=pygame.Rect(bordersize + (tab*tabsize), topgap, tabsize, 30))
    screen.fill(selected, rect=pygame.Rect(bordersize, topgap+30, winsize[0]-(2*bordersize), winsize[1]-30-topgap-bottomgap))
    screen.fill(unselected, rect=pygame.Rect(bordersize, winsize[1]-bottomgap+bordersize, winsize[0]-(2*bordersize), bottomgap-(bordersize*2)))

pygame.display.flip()

print(pygame.display.Info())

tab = 0
hovertab = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 1025 and event.dict["button"] == 1 and topgap < event.dict["pos"][1] < topgap+30:
            tab = int((event.dict["pos"][0]-bordersize)/tabsize)
        if event.type == 1024:
            if topgap < event.dict["pos"][1] < (topgap+30):
                hovertab = int((event.dict["pos"][0]-bordersize)/tabsize)
            else:
                hovertab = None
            
    drawtab(tab)
    if hovertab != tab and hovertab != None and hovertab <= 5:
        screen.fill(hover, rect=pygame.Rect(bordersize + (hovertab*tabsize), topgap, tabsize, 30))
        
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
