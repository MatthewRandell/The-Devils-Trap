import pygame as pg
import random
pg.init()

windowSize = [600,600]
screen = pg.display.set_mode(windowSize)
pg.display.set_caption("The Devil Trap")
clock = pg.time.Clock()
gameSpeed = 32

coinSound = pg.mixer.Sound('gong.wav')
ftSound = pg.mixer.Sound('flamethrower.wav')
teleSound = pg.mixer.Sound('ftSound.wav')
pg.mixer.music.load('bgMusic.mp3')
pg.mixer.music.play()

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

def checkOffScreenEnemyX(x):
    if x>windowSize[0]:
        x = 0
    elif x<0:
        x = windowSize[0]
    return x

def checkOffScreenYEnemy(y):
    if y>size[1]:
        y = 0
    elif y<0:
        y = size[1]
    return y


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
    if -32< y-coinY<32 and -32<x-coinX<32 and hasCoin == False:
        hasCoin = True 
        coinSound.play()
        pg.time.wait(int(coinSound.get_length())+300)
        coinSound.stop()
def checkEnemyHit():
    global x
    global enemyX
    global y
    global enemyY
    global hasCoin
    if -32< y-enemyY<32 and -32<x-enemyX<32 and hasCoin == True:
        screen.blit(bg,(0,0))
        screen.blit(image,(x,y))
        enemy = eMove(bright1,bright2)
        enemyX += .25
        enemyX = checkOffScreenEnemyX(enemyX)
        screen.blit(enemy,(enemyX,enemyY))
        pg.display.flip()
        print("devil hit")
    elif -32< y-enemyY<32 and -32<x-enemyX<32 and hasCoin == False:
        screen.blit(bg,(0,0))
        screen.blit(image,(x,y))
        enemy = eMove(bright1,bright2)
        enemyX += .25
        enemyX = checkOffScreenEnemyX(enemyX)
        screen.blit(enemy,(enemyX,enemyY))
        pg.display.flip()
        
        print("skull hit")



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

#boy sprite
bfront1 = pg.image.load('ybo1_fr1.gif')
bfront2 = pg.image.load('ybo1_fr2.gif')
bback1 = pg.image.load('ybo1_bk1.gif')
bback2 = pg.image.load('ybo1_bk2.gif')
bright1 = pg.image.load('ybo1_rt1.gif')
bright2 = pg.image.load('ybo1_rt2.gif')
bleft1 = pg.image.load('ybo1_lf1.gif')
bleft2 = pg.image.load('ybo1_lf2.gif')

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

pentaCoin = pg.image.load('penta.png_64x64.png')

bg = pg.image.load('DungeonTile.png')

white = pg.color.Color('#ffffff')
red = pg.color.Color('#ff0000')

currImg = standing
eCount = 0
enemy = eMove(bright1,bright2)

count = 0
counter = 0

x = windowSize[0] / 2 -16
y = windowSize[1] / 2 -16
coinX = random.randint(150,windowSize[0]-150)
coinY = random.randint(-150,windowSize[1]+150)
enemyX = 200
enemyY = 200

hasCoin = False
locked = False

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
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    enemy = eMove(bright1,bright2)
                    enemyX += .25
                    enemyX = checkOffScreenEnemyX(enemyX)
                    screen.blit(enemy,(enemyX,enemyY))
                    screen.blit(ftUP,(x-16,y-70))
                    pg.display.flip()
                    ftSound.stop()
                elif currImg == front1:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    enemy = eMove(bright1,bright2)
                    enemyX += .25
                    enemyX = checkOffScreenEnemyX(enemyX)
                    screen.blit(enemy,(enemyX,enemyY))
                    screen.blit(ftDOWN,(x-16,y+40))
                    pg.display.flip()
                    ftSound.stop()
                elif currImg == left2:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    enemy = eMove(bright1,bright2)
                    enemyX += .25
                    enemyX = checkOffScreenEnemyX(enemyX)
                    screen.blit(enemy,(enemyX,enemyY))
                    screen.blit(ftLEFT,(x-60,y-15))
                    pg.display.flip()
                    ftSound.stop()
                elif currImg == right2:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    enemy = eMove(bright1,bright2)
                    enemyX += .25
                    enemyX = checkOffScreenEnemyX(enemyX)
                    screen.blit(enemy,(enemyX,enemyY))
                    screen.blit(ft,(x+30,y-15))
                    pg.display.flip()
                    ftSound.stop()
                i+=1
        if keys[pg.K_c]:
            print(str(hasCoin))
            coinX = random.randint(300,windowSize[0]-200)
            coinY = random.randint(-300,windowSize[1]+200)
    else:
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
                locked = False
            
            count += 1
        else:
            locked = False
    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    coinX = checkOffScreenX(coinX)
    coinY = checkOffScreenY(coinY)
    checkCoin()
    checkEnemyHit()
    screen.blit(bg,(0,0))
    screen.blit(image,(x,y))
    enemyX += 1
    enemy = eMove(bright1,bright2)
    eCount+=1
    enemyX = checkOffScreenEnemyX(enemyX)
    screen.blit(enemy,(enemyX,enemyY))
    if not hasCoin:
        screen.blit(pentaCoin,(coinX,coinY)) 
    for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
    clock.tick(gameSpeed)
    pg.display.flip()
pg.quit()
