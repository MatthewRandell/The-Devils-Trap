#enemy file
import pygame as pg

#boy sprite
bfront1 = pg.image.load('ybo1_fr1.gif')
bfront2 = pg.image.load('ybo1_fr2.gif')
bback1 = pg.image.load('ybo1_bk1.gif')
bback2 = pg.image.load('ybo1_bk2.gif')
bright1 = pg.image.load('ybo1_rt1.gif')
bright2 = pg.image.load('ybo1_rt2.gif')
bleft1 = pg.image.load('ybo1_lf1.gif')
bleft2 = pg.image.load('ybo1_lf2.gif')

def eMove (image1,image2):
    global eCount
    if eCount < 5:
        image = image1
    elif eCount >= 5:
        image = image2

    if eCount >= 10:
        eCount = 0
    else:
        eCount +=1
    return image
