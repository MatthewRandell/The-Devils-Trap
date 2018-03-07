import pygame as pg
pg.init()

windowSize = [800,600]
screen = pg.display.set_mode(windowSize)

bard = pg.image.load('Bard_Render.png')
dcap = pg.image.load('dcap.png')

x = 0
y = 0

screen.blit(bard,(x+10,y+50))
screen.blit(dcap,(x-120,y-170))

done = False
while not done: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        pg.display.flip()
pg.quit()   
