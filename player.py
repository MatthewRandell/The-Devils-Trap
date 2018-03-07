#The Player file
import pygame as pg
import DevilTrapTestingEnviroment as dtt

#skeleton sprite
standing = pg.image.load('skl1_rt2.gif')
sBack1 = pg.image.load('skl1_bk1.gif')
sBack2 = pg.image.load('skl1_bk2.gif')
sFront1 = pg.image.load('skl1_fr1.gif')
sFront2 = pg.image.load('skl1_fr2.gif')
sLeft1 = pg.image.load('skl1_lf1.gif')
sLeft2 = pg.image.load('skl1_lf2.gif')
sRight1 = pg.image.load('skl1_rt1.gif')
sRight2 = pg.image.load('skl1_rt2.gif')

#devil sprite
front1 = pg.image.load('dvl1_fr1.gif')
front2 = pg.image.load('dvl1_fr2.gif')
back1 = pg.image.load('dvl1_bk1.gif')
back2 = pg.image.load('dvl1_bk2.gif')
right1 = pg.image.load('dvl1_rt1.gif')
right2 = pg.image.load('dvl1_rt2.gif')
left1 = pg.image.load('dvl1_lf1.gif')
left2 = pg.image.load('dvl1_lf2.gif')

#tele sprite
tele1 = pg.image.load('flame_a_0001.png_64x64.png')
tele2 = pg.image.load('flame_a_0002.png_64x64.png')
tele3 = pg.image.load('flame_a_0003.png_64x64.png')
tele4 = pg.image.load('flame_a_0004.png_64x64.png')
tele5 = pg.image.load('flame_a_0005.png_64x64.png')
tele6 = pg.image.load('flame_a_0006.png_64x64.png')

#flamethrower
ft = pg.image.load('flamethrower_0006.png_64x64.png')
ftUP = pg.transform.rotate(ft,90)
ftDOWN = pg.transform.rotate(ft,270)
ftLEFT = pg.transform.rotate(ft,180)

#sounds
ftSound = pg.mixer.Sound('flamethrower.wav')
teleSound = pg.mixer.Sound('ftSound.wav')

#counter for movement
count = 0

#starting position
x = dtt.windowSize[0] / 2 -16
y = dtt.windowSize[1] / 2 -16

#start getting keys
keys = pg.key.get_pressed()

image = sfront1

def move (image1,image2):
    global count
    if count < 5:
        image = image1
    elif count >= 5:
        image = image2

    if count >= 10:
        count = 0
    else:
        count +=1
    return image

def controls():
        if keys[pg.K_w]:
            if not hasCoin:
                image = move(sBack1,sBack2)
                currImg = sBack1
                y -= 1
            else:
                image = move(back1,back2)
                currImg = back1
                y -= 1
        elif keys[pg.K_d]:
            if not hasCoin:
                image = move(sRight1,sRight2)
                currImg = sRight2
                x += 1
            else:
                image = move(right1,right2)
                currImg = right2
                x += 1
        elif keys[pg.K_s]:
            if not hasCoin:
                image = move(sFront1,sFront2)
                currImg = sFront1
                y += 1
            else:
                image = move(front1,front2)
                currImg = front1
                y += 1
        elif keys[pg.K_a]:
            if not hasCoin:
                image = move(sLeft1,sLeft2)
                currImg = sLeft2
                x -= 1
            else:
                image = move(left1,left2)
                currImg = left2
                x -= 1
        elif keys[pg.K_SPACE]:
            if hasCoin:
                teleSound.play()
                if count < 3:
                    image = tele1
                    clock.tick(64)
                elif count < 6:
                    image = tele2
                    clock.tick(64)
                elif count < 9:
                    image = tele3
                    clock.tick(64)
                elif count < 12:
                    image = tele4
                    clock.tick(64)
                elif count < 15:
                    image = tele5
                    clock.tick(64)
                elif count < 18:
                    image = tele6
                    clock.tick(64)
                else:
                    if currImg == back1: 
                        y -= 60
                    elif currImg == front1:
                        y += 60
                    elif currImg == right2:
                        x += 60
                    elif currImg == left2:
                        x -= 60
                    
                    teleSound.stop()
                    print("trigger" + str(count))
                    count = 0
        elif keys[pg.K_r]:
            runToggle = not runToggle
            if runToggle:
                gameSpeed = 72
            else:
                gameSpeed = 32
        else:
            image = currImg
            count = 0
        if keys[pg.K_e]:
            i=0
            while i<32:
                if currImg == back1:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ftUP,(x-16,y-70))
                    pg.display.flip()
                    ftSound.stop()
                elif currImg == front1:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ftDOWN,(x-16,y+40))
                    pg.display.flip()
                    ftSound.stop()
                elif currImg == left2:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ftLEFT,(x-60,y-15))
                    pg.display.flip()
                    ftSound.stop()
                elif currImg == right2:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ft,(x+30,y-15))
                    pg.display.flip()
                    ftSound.stop()
                i+=1
        if keys[pg.K_c]:
            print(str(hasCoin))
            coinX = random.randint(300,windowSize[0]-200)
            coinY = random.randint(-300,windowSize[1]+200)
        else:
            count += 1
    
