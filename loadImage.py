import pygame as pg
pg.init()

windowSize = [800,600]
screen = pg.display.set_mode(windowSize)
image = pg.image.load('Bard_Render.png')
screen.blit(image,(0,0))
done = False
while not done: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        pg.display.flip()
pg.quit()   
