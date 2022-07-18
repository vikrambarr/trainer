import pygame
from threading import Thread
import time
import requests
import shutil

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
tabheight = 40

listofmons = ["Ampharos", "Camerupt-Mega", "Ferroseed", "Pyukumuku", "Blissey", "Charizard-Mega-X"]

def scrapeimages(mons):
    sesh = requests.session()
    for i, mon in enumerate(mons):
        info = sesh.get("https://pokeapi.co/api/v2/pokemon/" + mon.lower()).json()
        image = sesh.get(info["sprites"]["front_default"], stream=True)
        with open(f"images\\{i}.png", "wb") as of:
            shutil.copyfileobj(image.raw, of)

scrapeimages(listofmons)  

images = []
tabcolors = []

for i, mon in enumerate(listofmons):
    images.append(pygame.image.load(f"images/{i}.png"))

for image in images:
    if pygame.transform.average_color(image) != (0, 0, 0, 0):
        tabcolors.append(pygame.transform.average_color(image))
    else:
        tabcolors.append(pygame.transform.average_color(image, rect=pygame.Rect(43, 43, 10, 10)))
print(tabcolors)
    
def drawtab(tab):
    screen.fill(border)
    screen.fill(unselected, rect=pygame.Rect(bordersize, topgap, winsize[0]-(2*bordersize), tabheight))
    screen.fill(selected, rect=pygame.Rect(bordersize + (tab*tabsize), topgap, tabsize, tabheight))
    screen.fill(selected, rect=pygame.Rect(bordersize, topgap+tabheight, winsize[0]-(2*bordersize), winsize[1]-tabheight-topgap-bottomgap))
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
            
        if event.type == 1025 and event.dict["button"] == 1 and topgap < event.dict["pos"][1] < topgap+tabheight:
            tab = int((event.dict["pos"][0]-bordersize)/tabsize)
            
        if event.type == 1024:
            if topgap < event.dict["pos"][1] < (topgap+tabheight):
                hovertab = int((event.dict["pos"][0]-bordersize)/tabsize)
            else:
                hovertab = None
            
    drawtab(tab)
    
    if hovertab != tab and hovertab != None and hovertab <= 5:
        screen.fill(hover, rect=pygame.Rect(bordersize + (hovertab*tabsize), topgap, tabsize, tabheight))
        
    for i, image in enumerate(images):
        screen.blit(pygame.transform.scale(image, (50, 50)), (bordersize + (tabsize*i) + 5, topgap - 5))
        
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
