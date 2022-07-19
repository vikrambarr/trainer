from poke import search_dict
from threading import Thread

import pygame

import time
import requests
import shutil

pygame.init()
clock = pygame.time.Clock()

type_colors = {}

type_colors_dark = {
	"normal": (168, 156, 159), 
	"fighting": (138, 54, 54), 
	"ghost": (64, 54, 138), 
	"bug": (138, 125, 54), 
	"dark": (59, 44, 39), 
	"psychic": (138, 54, 96), 
	"fairy": (230, 64, 211), 
	"flying": (134, 203, 240), 
	"fire": (230, 125, 64), 
	"water": (54, 93, 138), 
	"grass": (61, 138, 54), 
	"ground": (138, 78, 54), 
	"poison": (111, 54, 138), 
	"steel": (211, 220, 242), 
	"rock": (140, 114, 60), 
	"ice": (64, 230, 224), 
	"electric": (230, 224, 64), 
	"dragon": (111, 64, 230)
}

for key, value in zip(type_colors_dark.keys(), type_colors_dark.values()):

    a = 255 if (value[0] + 20) > 255 else value[0] + 20
    b = 255 if (value[1] + 20) > 255 else value[1] + 20
    c = 255 if (value[2] + 20) > 255 else value[2] + 20
    type_colors.update({key: (a, b, c)})

winsize = (380, 720)
screen = pygame.display.set_mode(winsize)

border = (200, 200, 200)
unselected = (70, 70, 70)
selected = (230, 230, 230)
hover = (165, 165, 165)

topgap = 10
bottomgap = 150
bordersize = 10
tabsize = ((winsize[0]-(2*bordersize))/6)
tabheight = 40

listofmons = ["Unown", "Cresselia", "Noivern", "Charizard", "Pyukumuku", "Liepard"]
poketype = []

def scrapeimages(mons):
    sesh = requests.session()
    for i, mon in enumerate(mons):
        info = sesh.get("https://pokeapi.co/api/v2/pokemon/" + mon.lower()).json()
        image = sesh.get(info["sprites"]["front_default"], stream=True)
        poketype.append(info["types"][0]["type"]["name"])
        with open(f"images\\{i}.png", "wb") as of:
            shutil.copyfileobj(image.raw, of)


scrapeimages(listofmons)  
print(poketype)

images = []
tabcolors = []

for i, mon in enumerate(listofmons):
    images.append(pygame.image.load(f"images/{i}.png"))
    
def drawtab(tab):
    screen.fill(border)
    for i, mon in enumerate(listofmons):
        screen.fill(type_colors_dark[poketype[i]], rect=pygame.Rect(bordersize + (i*tabsize), topgap, tabsize, tabheight))
        
    screen.fill(type_colors[poketype[tab]], rect=pygame.Rect(bordersize + (tab*tabsize), topgap, tabsize, tabheight))
    screen.fill(type_colors[poketype[tab]], rect=pygame.Rect(bordersize, topgap+tabheight, winsize[0]-(2*bordersize), winsize[1]-tabheight-topgap-bottomgap))
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
