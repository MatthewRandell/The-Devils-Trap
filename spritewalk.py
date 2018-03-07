import pygame as pg
import random
pg.init()

windowSize = [600,600]
screen = pg.display.set_mode(windowSize)
pg.display.set_caption("The Devil Trap")
clock = pg.time.Clock()

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

def checkOffScreenX(x):
    if x>windowSize[0]-32:
        x = windowSize[0]-32
    elif x<0:
        x = 0
    return x

def checkOffScreenY(y):
    if y>windowSize[1]-32:
        y = windowSize[1]-32
    elif y<0:
        y = 0
    return y
def checkOffScreenCX(x):
    if x>windowSize[0]-64:
        x = windowSize[0]-64
    elif x<0:
        x = 0
    return x

def checkOffScreenCY(y):
    if y>windowSize[1]-64:
        y = windowSize[1]-64
    elif y<0:
        y = 0
    return y

def checkCoin():
    global x
    global coinX
    global y
    global coinY
    global hasCoin
    if -32< y-coinY<32 and -32<x-coinX<32:
        hasCoin = True

standing = pg.image.load('skl1_rt2.gif')

sBack1 = pg.image.load('skl1_bk1.gif')
sBack2 = pg.image.load('skl1_bk2.gif')

sFront1 = pg.image.load('skl1_fr1.gif')
sFront2 = pg.image.load('skl1_fr2.gif')

sLeft1 = pg.image.load('skl1_lf1.gif')
sLeft2 = pg.image.load('skl1_lf2.gif')

sRight1 = pg.image.load('skl1_rt1.gif')
sRight2 = pg.image.load('skl1_rt2.gif')


front1 = pg.image.load('dvl1_fr1.gif')
front2 = pg.image.load('dvl1_fr2.gif')

back1 = pg.image.load('dvl1_bk1.gif')
back2 = pg.image.load('dvl1_bk2.gif')

right1 = pg.image.load('dvl1_rt1.gif')
right2 = pg.image.load('dvl1_rt2.gif')

left1 = pg.image.load('dvl1_lf1.gif')
left2 = pg.image.load('dvl1_lf2.gif')

tele1 = pg.image.load('flame_a_0001.png_64x64.png')
tele2 = pg.image.load('flame_a_0002.png_64x64.png')
tele3 = pg.image.load('flame_a_0003.png_64x64.png')
tele4 = pg.image.load('flame_a_0004.png_64x64.png')
tele5 = pg.image.load('flame_a_0005.png_64x64.png')
tele6 = pg.image.load('flame_a_0006.png_64x64.png')


ft = pg.image.load('flamethrower_0006.png_64x64.png')
ftUP = pg.transform.rotate(ft,90)
ftDOWN = pg.transform.rotate(ft,270)
ftLEFT = pg.transform.rotate(ft,180)

pentaCoin = pg.image.load('penta.png_64x64.png')

bg = pg.image.load('DungeonTile.png')

white = pg.color.Color('#ffffff')

currImg = standing

count = 0
counter = 0
x = windowSize[0] / 2 -16
y = windowSize[1] / 2 -16
coinX = random.randint(150,windowSize[0]-150)
coinY = random.randint(-150,windowSize[1]+150)

hasCoin = False
locked = False
gameSpeed = 32
runToggle = False

done = False
while not done :
    screen.fill(white)
    keys = pg.key.get_pressed()
    #player control
    if not locked:
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
            locked = True
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
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ftUP,(x-16,y-70))
                    pg.display.flip()
                elif currImg == front1:   
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ftDOWN,(x-16,y+40))
                    pg.display.flip()
                elif currImg == left2:   
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ftLEFT,(x-60,y-15))
                    pg.display.flip()
                elif currImg == right2:   
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    screen.blit(ft,(x+30,y-15))
                    pg.display.flip()
                
                    
                i+=1
        if keys[pg.K_c]:
            print(str(hasCoin))
    else:
        if hasCoin:
            if count < 5:
                image = tele1
                clock.tick(32)
            elif count < 10:
                image = tele2
                clock.tick(32)
            elif count < 15:
                image = tele3
                clock.tick(32)
            elif count < 20:
                image = tele4
                clock.tick(32)
            elif count < 25:
                image = tele5
                clock.tick(32)
            elif count < 30:
                image = tele6
                clock.tick(32)
            else:
                x = random.randint(0,windowSize[0])
                y = random.randint(0,windowSize[1])
                print("trigger" + str(count))
                count = 0
                locked = False
            
            count += 1
        else:
            locked = False
    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    coinX = checkOffScreenX(coinX)
    coinY = checkOffScreenY(coinY)
    checkCoin()
    screen.blit(bg,(0,0))
    screen.blit(image,(x,y))
    if not hasCoin:
        screen.blit(pentaCoin,(coinX,coinY)) 
    for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
    clock.tick(gameSpeed)
    pg.display.flip()
pg.quit()
