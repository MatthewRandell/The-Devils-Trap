import pygame as pg
import random
pg.init()

windowSize = [600,600]
screen = pg.display.set_mode(windowSize)
pg.display.set_caption("The Devil Trap")
clock = pg.time.Clock()
gameSpeed = 32
myfont = pg.font.SysFont("monospace", 40)
myfont2 = pg.font.SysFont("monospace", 20)
deathLabel = myfont.render("You Have Died", 1, (255,0,0))
coinLabel = myfont.render("The Demon Rises!", 1, (255,0,0))
goalLabel = myfont.render("Consume the intruder!", 1, (255,0,0))

#text for beginning a level
startLabel1B = myfont.render("Awakening", 1, (255,0,0))
startLabel1A = myfont.render("Level 1:", 1, (255,0,0))

startLabel2B = myfont.render("Hunger", 1, (255,0,0))
startLabel2A = myfont.render("Level 2:", 1, (255,0,0))

startLabel3B = myfont.render("Power", 1, (255,0,0))
startLabel3A = myfont.render("Level 3:", 1, (255,0,0))

startLabel4B = myfont.render("Control", 1, (255,0,0))
startLabel4A = myfont.render("Level 4:", 1, (255,0,0))

startLabel5B = myfont.render("Redemption", 1, (255,0,0))
startLabel5A = myfont.render("Level 5:", 1, (255,0,0))

#story text
level1StoryA = myfont2.render("A once powerful demon is nothing but ", 1, (255,0,0))
level1StoryB = myfont2.render("cursed bones for centuries until ", 1, (255,0,0))
level1StoryC = myfont2.render("a young boy stumbles upon the ", 1, (255,0,0))
level1StoryD = myfont2.render("dungeon while playing in the castle...", 1, (255,0,0))

level2StoryA = myfont2.render("Consuming the children has given you a small  ", 1, (255,0,0))
level2StoryB = myfont2.render("taste of your true power but it fades quickly.", 1, (255,0,0))
level2StoryC = myfont2.render("before you're strong enough to fight the king  ", 1, (255,0,0))
level2StoryD = myfont2.render("you must consume stronger opponents", 1, (255,0,0))

level3StoryA = myfont2.render("Consuming the gaurds has brought attention ", 1, (255,0,0))
level3StoryB = myfont2.render("to the kings knights,they have dawned ", 1, (255,0,0))
level3StoryC = myfont2.render("holy armor to stop you from Consuming them. ", 1, (255,0,0))
level3StoryD = myfont2.render("Lucky for you by devouring the gaurds ", 1, (255,0,0))
level3StoryE = myfont2.render("your hellfire breath has returned.  ", 1, (255,0,0))
level3StoryF = myfont2.render("press the e key to melt your enemies armor", 1, (255,0,0))
level3StoryG = myfont2.render("Be carefull, you will not be able to move", 1, (255,0,0))
level3StoryH = myfont2.render("while channeling your hellfire", 1, (255,0,0))

level4StoryA = myfont2.render("Wizards! it appears the king has ", 1, (255,0,0))
level4StoryB = myfont2.render("summoned his wizard allies to his side.", 1, (255,0,0))
level4StoryC = myfont2.render("The wizards are cowwardly foes who ", 1, (255,0,0))
level4StoryD = myfont2.render("prefer to attack from a distance then", 1, (255,0,0))
level4StoryE = myfont2.render("teleport to saftey. Against common ", 1, (255,0,0))
level4StoryF = myfont2.render("attackers they are almost impossible", 1, (255,0,0))
level4StoryG = myfont2.render("to deal with. sadly for them you  ", 1, (255,0,0))
level4StoryH = myfont2.render("are far from ordinary. Your strength ", 1, (255,0,0))
level4StoryI = myfont2.render("has increased again. Press the space bar  ", 1, (255,0,0))
level4StoryJ = myfont2.render("to teleport rapidly in the direction you're", 1, (255,0,0))
level4StoryK = myfont2.render("facing. release the button early to cancel.", 1, (255,0,0))
level4StoryL = myfont2.render("Nothing will stop your vengance", 1, (255,0,0))

level5StoryA = myfont2.render("At last the bastard king.Centuries ago  ", 1, (255,0,0))
level5StoryB = myfont2.render("he locked you away in the demon trap ", 1, (255,0,0))
level5StoryC = myfont2.render("since that time he has been using your  ", 1, (255,0,0))
level5StoryD = myfont2.render("energy to fuel his life and hold his reign.", 1, (255,0,0))
level5StoryE = myfont2.render("This pitiful kingdom means nothing to  ", 1, (255,0,0))
level5StoryF = myfont2.render("you but his defiance will not go  ", 1, (255,0,0))
level5StoryG = myfont2.render("unpunished.Kill him and unlock your", 1, (255,0,0))
level5StoryH = myfont2.render("true self once more.Then raze his city", 1, (255,0,0))
level5StoryI = myfont2.render("to the ground. Beware the king, he will  ", 1, (255,0,0))
level5StoryJ = myfont2.render("not be harmed as long as his alters are intact  ", 1, (255,0,0))
level5StoryK = myfont2.render("stepping on them will change them to   ", 1, (255,0,0))
level5StoryL = myfont2.render("help you. making contact with the king", 1, (255,0,0))
level5StoryM = myfont2.render("will kill you unless you are at full power. ", 1, (255,0,0))



#text for ending a level
endLabel1A = myfont.render("Level 1:", 1, (255,0,0))
endLabel2A = myfont.render("Level 2:", 1, (255,0,0))
endLabel3A = myfont.render("Level 3:", 1, (255,0,0))
endLabel4A = myfont.render("Level 4:", 1, (255,0,0))
endLabel5A = myfont.render("Level 5:", 1, (255,0,0))
endLabelB = myfont.render("Complete!", 1, (255,0,0))
        


coinSound = pg.mixer.Sound('gong.wav')
ftSound = pg.mixer.Sound('flamethrower.wav')
teleSound = pg.mixer.Sound('tele.wav')
pg.mixer.music.load('bgMusic.mp3')
#pg.mixer.music.play()
pg.mixer.set_num_channels(1)

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
    global enemyY
    if x>windowSize[0]:
        x = 0
        enemyY = random.randint(200,350)
    elif x<0:
        x = windowSize[0]
        enemyY = random.randint(200,350)
    return x

def checkOffScreenEnemyY(y):
    global enemyX
    if y>windowSize[1]:
        y = 0
        enemyX = random.randint(200,350)
    elif y<0:
        y = windowSize[1]
        enemyX = random.randint(200,350)
    return y
def enemySideStart():
    global enemyX
    global enemyY
    global eStart
    
    if enemyX>windowSize[0]:
        enemyX = random.randint(200,350)
        enemyY = 0
        eStart = False
    if enemyY>windowSize[1]:
        enemyX = 0
        enemyY = random.randint(200,350)
        eStart = True


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
    if x>windowSize[0]-80:
        x = windowSize[0]-80
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
    global currImg
    global chargeLevel;
    if -32< y-coinY<32 and -32<x-coinX<32 and hasCoin == False:
        if(chargeLevel >= 4):
            chargeLevel = 5 
            hasCoin = True 
            coinSound.play()
            pg.time.wait(int(coinSound.get_length())+300)
            for i in range(9000):
                screen.fill(black)
                screen.blit(coinLabel, (100,windowSize[1] /2-100))
                screen.blit(goalLabel, (50,windowSize[1] /2))
                if 1000 < i < 2000 or 3000 < i < 4000 or 5000 < i < 6000 or 7000 < i < 8000 or 8500 < i <= 9000 : 
                    screen.blit(front1,(windowSize[0]/2 - 32 ,windowSize[1] /2 + 100))
                else:
                    screen.blit(sFront1,(windowSize[0]/2 - 32,windowSize[1] /2 + 100))
                pg.display.flip()
            currImg = front1      
            coinSound.stop()
        else:
            chargeLevel += 1
            coinX = random.randint(150,windowSize[0]-150)
            coinY = random.randint(-150,windowSize[1]+150)
            print("charge: "+str(chargeLevel))
            
def checkEnemyHit():
    global x
    global enemyX
    global y
    global enemyY
    global hasCoin
    global enemyDead
    global playerLife
    global enemyHealth
    if -32< y-enemyY<32 and -32<x-enemyX<32 and hasCoin == True:
        if enemyHealth == 0:
            enemyDead = True
        else:
            enemyHealth -= 1
        screen.blit(bg,(0,0))
        screen.blit(image,(x,y))
        enemy = eMove(bright1,bright2)
        enemyX = 800
        screen.blit(enemy,(enemyX,enemyY))
        pg.display.flip()
        print("devil hit")
    elif -32< y-enemyY<32 and -32<x-enemyX<32 and hasCoin == False:
        screen.blit(bg,(0,0))
        x = windowSize[0] / 2 -16
        y = windowSize[1] / 2 -16
        screen.blit(image,(x,y))
        enemy = eMove(bright1,bright2)
        enemyX += 100
        enemyX = checkOffScreenEnemyX(enemyX)
        screen.blit(enemy,(enemyX,enemyY))
        pg.display.flip()
        playerLife -= 1
        print("skull hit")
def checkWallHit():
    global x
    global enemyX
    global coinX
    global y
    global enemyY
    global coinY
    #check if player is hitting wall
    #upper Left corner
    if y<190 and -32<x<62:
        y += 3
        print("upper left wall bot")
    if x<70 and 65<y<175:
        x += 3
        print("upper left wall inside vert")
    if 70<x<170 and y<70:
        y += 3
        print("upper left wall inside hori")
    if x<190 and -32<y<60:
        x += 3
        print("upper left wall right")

    #lower Left corner    
    if y>376 and -32<x<62:
        y -= 3
        print("lower left wall top")
    if x<70 and 387<y<502:
        x += 3
        print("lower left wall inside vert")
    if 70<x<170 and y>489:
        y -= 3
        print("lower left wall inside hori")
    if x<190 and 490<y<570:
        x += 3
        print("lower left wall right")
        
    #upper Right corner
    if y<190 and 501<x<600:
        y += 3
        print("upper right wall bot")
    if x>=500 and 65<y<175:
        x -= 3
        print("upper right wall inside vert")
    if 400<x<500 and y<70:
        y += 3
        print("upper right wall inside hori")
    if x>380 and -32<y<60:
        x -= 3
        print("upper right wall left")


    #lower Right corner    
    if y>376 and 505<x<600:
        y -= 3
        print("lower right wall top")
    if x>500 and 389<y<500:
        x -= 3
        print("lower right wall inside vert")
    if 400<x<500 and y>490:
        y -= 3
        print("lower right wall inside hori")
    if x>380 and 500<y<570:
        x -= 3
        print("lower right wall left")

#check if coin is hitting wall
    #upper Left corner
    if coinY<190 and -32<coinX<62:
        coinY += 90
        print("upper left wall bot coin")
    if coinX<70 and 65<coinY<175:
        coinX += 90
        print("upper left wall inside vert coin")
    if 70<coinX<170 and coinY<70:
        coinY += 90
        print("upper left wall inside hori coin")
    if coinX<190 and -32<coinY<60:
        coinX += 90
        print("upper left wall right coin")

    #lower Left corner    
    if coinY>376 and -32<coinX<62:
        coinY -= 90
        print("lower left wall top coin")
    if coinX<70 and 387<coinY<502:
        coinX += 90
        print("lower left wall inside vert coin")
    if 70<coinX<170 and coinY>489:
        coinY -= 90
        print("lower left wall inside hori coin")
    if coinX<190 and 490<coinY<570:
        coinX += 90
        print("lower left wall right coin")
        
    #upper Right corner
    if coinY<190 and 501<coinX<600:
        coinY += 90
        print("upper right wall bot coin")
    if coinX>=500 and 65<coinY<175:
        coinX -= 90
        print("upper right wall inside vert coin")
    if 400<coinX<500 and coinY<70:
        coinY += 90
        print("upper right wall inside hori coin")
    if coinX>380 and -32<coinY<60:
        coinX -= 90
        print("upper right wall left coin")


    #lower Right corner    
    if coinY>376 and 505<coinX<600:
        coinY -= 90
        print("lower right wall top coin")
    if coinX>500 and 389<coinY<500:
        coinX -= 90
        print("lower right wall inside vert coin")
    if 400<coinX<500 and coinY>490:
        coinY -= 90
        print("lower right wall inside hori coin")
    if coinX>380 and 500<coinY<570:
        coinX -= 90
        print("lower right wall left coin")
def drawPower():
    if chargeLevel == 1:
        screen.blit(powerBar1,(0,56))
    if chargeLevel == 2:
        screen.blit(powerBar1,(0,56))
        screen.blit(powerBar2,(0,42))
    if chargeLevel == 3:
        screen.blit(powerBar1,(0,56))
        screen.blit(powerBar2,(0,42))
        screen.blit(powerBar3,(0,28))
    if chargeLevel == 4:
        screen.blit(powerBar1,(0,56))
        screen.blit(powerBar2,(0,42))
        screen.blit(powerBar3,(0,28))
        screen.blit(powerBar4,(0,14))
    if chargeLevel == 5:
        screen.blit(powerBar1,(0,56))
        screen.blit(powerBar2,(0,42))
        screen.blit(powerBar3,(0,28))
        screen.blit(powerBar4,(0,14))
        screen.blit(powerBar5,(0,0))



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

#man sprite
mfront1 = pg.image.load('ftr1_fr1.gif')
mfront2 = pg.image.load('ftr1_fr2.gif')
mback1 = pg.image.load('ftr1_bk1.gif')
mback2 = pg.image.load('ftr1_bk2.gif')
mright1 = pg.image.load('ftr1_rt1.gif')
mright2 = pg.image.load('ftr1_rt2.gif')
mleft1 = pg.image.load('ftr1_lf1.gif')
mleft2 = pg.image.load('ftr1_lf2.gif')

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

#coin 
pentaCoin = pg.image.load('penta.png_64x64.png')

#ChargeBar image
powerBar1 = pg.image.load('Power1.png')
powerBar2 = pg.image.load('Power2.png')
powerBar3 = pg.image.load('Power3.png')
powerBar4 = pg.image.load('Power4.png')
powerBar5 = pg.image.load('Power5.png')

#background
bg = pg.image.load('DungeonTile.png')

white = pg.color.Color('#ffffff')
red = pg.color.Color('#ff0000')
black = pg.color.Color('#000000')

currImg = standing

#enemy declerations
eCount = 0
enemy = eMove(bright1,bright2)
eStart = True

count = 0
counter = 0

playerLife = 3
level = 1
enemyHealth = level - 1
chargeLevel = 0

x = windowSize[0] / 2 -16
y = windowSize[1] / 2 -16
coinX = random.randint(150,windowSize[0]-150)
coinY = random.randint(-150,windowSize[1]+150)
enemyY = random.randint(200,350)
enemyX = 0

hasCoin = False
locked = False
enemyDead = False
runToggle = False
textDisplay = True
done = False


while not done :
    screen.fill(white)
    if level == 1 and textDisplay:    
        for i in range(5000):
            screen.fill(black)
            screen.blit(startLabel1B, (175,(windowSize[1] /2)))
            screen.blit(startLabel1A, (175,windowSize[1] /2-100))
            pg.display.flip()
            
        for i in range(5000):
            screen.fill(black)
            screen.blit(level1StoryA, (40,(windowSize[1] /2-40)))
            screen.blit(level1StoryB, (40,(windowSize[1] /2-20)))
            screen.blit(level1StoryC, (40,(windowSize[1] /2)))
            screen.blit(level1StoryD, (40,(windowSize[1] /2+20)))
            pg.display.flip()
        textDisplay = False

    if level == 2 and textDisplay:    
        for i in range(5000):
            screen.fill(black)
            screen.blit(startLabel2B, (175,(windowSize[1] /2)))
            screen.blit(startLabel2A, (175,windowSize[1] /2-100))
            pg.display.flip()
        for i in range(5000):
            screen.fill(black)
            screen.blit(level2StoryA, (20,(windowSize[1] /2-40)))
            screen.blit(level2StoryB, (20,(windowSize[1] /2-20)))
            screen.blit(level2StoryC, (20,(windowSize[1] /2)))
            screen.blit(level2StoryD, (20,(windowSize[1] /2+20)))
            pg.display.flip()
        textDisplay = False
        
    if level == 3 and textDisplay:    
        for i in range(5000):
            screen.fill(black)
            screen.blit(startLabel3B, (175,(windowSize[1] /2)))
            screen.blit(startLabel3A, (175,windowSize[1] /2-100))
            pg.display.flip()
        for i in range(12000):
            screen.fill(black)
            screen.blit(level3StoryA, (20,(windowSize[1] /2-40)))
            screen.blit(level3StoryB, (20,(windowSize[1] /2-20)))
            screen.blit(level3StoryC, (20,(windowSize[1] /2)))
            screen.blit(level3StoryD, (20,(windowSize[1] /2+20)))
            screen.blit(level3StoryE, (20,(windowSize[1] /2+40)))
            screen.blit(level3StoryF, (20,(windowSize[1] /2+60)))
            screen.blit(level3StoryG, (20,(windowSize[1] /2+80)))
            screen.blit(level3StoryH, (20,(windowSize[1] /2+100)))
            pg.display.flip()
        textDisplay = False
        
    if level == 4 and textDisplay:    
        for i in range(5000):
            screen.fill(black)
            screen.blit(startLabel4B, (175,(windowSize[1] /2)))
            screen.blit(startLabel4A, (175,windowSize[1] /2-100))
            pg.display.flip()
        for i in range(12000):
            screen.fill(black)
            screen.blit(level4StoryA, (20,(windowSize[1] /2-40)))
            screen.blit(level4StoryB, (20,(windowSize[1] /2-20)))
            screen.blit(level4StoryC, (20,(windowSize[1] /2)))
            screen.blit(level4StoryD, (20,(windowSize[1] /2+20)))
            screen.blit(level4StoryE, (20,(windowSize[1] /2+40)))
            screen.blit(level4StoryF, (20,(windowSize[1] /2+60)))
            screen.blit(level4StoryG, (20,(windowSize[1] /2+80)))
            screen.blit(level4StoryH, (20,(windowSize[1] /2+100)))
            screen.blit(level4StoryI, (20,(windowSize[1] /2+120)))
            screen.blit(level4StoryJ, (20,(windowSize[1] /2+140)))
            screen.blit(level4StoryK, (20,(windowSize[1] /2+160)))
            screen.blit(level4StoryL, (20,(windowSize[1] /2+180)))
            pg.display.flip()
        textDisplay = False
        
    if level == 5 and textDisplay:
        for i in range(5000):
            screen.fill(black)
            screen.blit(startLabel5B, (175,(windowSize[1] /2)))
            screen.blit(startLabel5A, (175,windowSize[1] /2-100))
            pg.display.flip()
        for i in range(12000):
            screen.fill(black)
            screen.blit(level5StoryA, (20,(windowSize[1] /2-40)))
            screen.blit(level5StoryB, (20,(windowSize[1] /2-20)))
            screen.blit(level5StoryC, (20,(windowSize[1] /2)))
            screen.blit(level5StoryD, (20,(windowSize[1] /2+20)))
            screen.blit(level5StoryE, (20,(windowSize[1] /2+40)))
            screen.blit(level5StoryF, (20,(windowSize[1] /2+60)))
            screen.blit(level5StoryG, (20,(windowSize[1] /2+80)))
            screen.blit(level5StoryH, (20,(windowSize[1] /2+100)))
            screen.blit(level5StoryI, (20,(windowSize[1] /2+120)))
            screen.blit(level5StoryJ, (20,(windowSize[1] /2+140)))
            screen.blit(level5StoryK, (20,(windowSize[1] /2+160)))
            screen.blit(level5StoryL, (20,(windowSize[1] /2+180)))
            screen.blit(level5StoryM, (20,(windowSize[1] /2+200)))

            pg.display.flip()
        textDisplay = False
        
    keys = pg.key.get_pressed()
    #player control
    if not locked:
        if keys[pg.K_w]:
            if not hasCoin:
                image = move(sBack1,sBack2)
                currImg = sBack1
                y -= 2
            else:
                image = move(back1,back2)
                currImg = back1
                y -= 2
        elif keys[pg.K_d]:
            if not hasCoin:
                image = move(sRight1,sRight2)
                currImg = sRight2
                x += 2
            else:
                image = move(right1,right2)
                currImg = right2
                x += 2
        elif keys[pg.K_s]:
            if not hasCoin:
                image = move(sFront1,sFront2)
                currImg = sFront1
                y += 2
            else:
                image = move(front1,front2)
                currImg = front1
                y += 2
        elif keys[pg.K_a]:
            if not hasCoin:
                image = move(sLeft1,sLeft2)
                currImg = sLeft2
                x -= 2
            else:
                image = move(left1,left2)
                currImg = left2
                x -= 2
        #teleporting unlocked at level 4 to handle wizard teleporting
        elif keys[pg.K_SPACE]:
            if hasCoin and level >= 4:
                if count ==0:
                    teleSound.stop()
                
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
            count += 1
        elif keys[pg.K_r]:
            runToggle = not runToggle
            if runToggle:
                gameSpeed = 72
            else:
                gameSpeed = 32
        else:
            image = currImg
            count = 0
        #fire breath unlocked at level 3 to handle armored units 
        if keys[pg.K_e] and level>=3:
            i=0
            while i<32:
                if currImg == back1:
                    ftSound.play()
                    screen.blit(bg,(0,0))
                    screen.blit(image,(x,y))
                    if not enemyDead:
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
                    if not enemyDead:
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
                    if not enemyDead:
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
                    if not enemyDead:
                        enemy = eMove(bright1,bright2)
                        enemyX += .25
                        enemyX = checkOffScreenEnemyX(enemyX)
                        screen.blit(enemy,(enemyX,enemyY))
                    screen.blit(ft,(x+30,y-15))
                    pg.display.flip()
                    ftSound.stop()
                i+=1
        if keys[pg.K_c]:
            coinX = random.randint(150,windowSize[0]-150)
            coinY = random.randint(-150,windowSize[1]+150)
        if keys[pg.K_o]:
            hasCoin = False
            textDisplay = True
            if level == 1:
                level = 2 
            elif level == 2:
                level = 3 - 1
            elif level == 3:
                level = 4 - 1
            elif level == 4:
                level = 5 - 1
            elif level == 5:
                level = 1
        if keys[pg.K_l]:
            print("level is " + str(level))
            print("enemy health is " + str(enemyHealth))
            print(x,y)
 
    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    coinX = checkOffScreenX(coinX)
    coinY = checkOffScreenY(coinY)
    checkCoin()
    checkEnemyHit()
    screen.blit(bg,(0,0))
    screen.blit(image,(x,y))
    checkWallHit()
    drawPower()
    if not enemyDead:
        if level == 1:
            if eStart == True:
                enemyX += 1
                enemy = eMove(bright1,bright2)
                eCount+=1
                enemySideStart()
                screen.blit(enemy,(enemyX,enemyY))
            if eStart == False:
                enemyY += 1
                enemy = eMove(bfront1,bfront2)
                eCount+=1
                enemySideStart()
                screen.blit(enemy,(enemyX,enemyY))
        elif level == 2:
            if eStart == True:
                enemyX += 5
                enemy = eMove(mright1,mright2)
                eCount+=1
                enemySideStart()
                screen.blit(enemy,(enemyX,enemyY))
            if eStart == False:
                enemyY += 5
                enemy = eMove(mfront1,mfront2)
                eCount+=1
                enemySideStart()
                screen.blit(enemy,(enemyX,enemyY))
    if not hasCoin:
        screen.blit(pentaCoin,(coinX,coinY)) 
    for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
    if enemyDead:
        if level == 1:
            for i in range(9000):
                screen.fill(black)
                screen.blit(endLabelB, (100,(windowSize[1] /2)))
                screen.blit(endLabel1A, (100,windowSize[1] /2-100))
                pg.display.flip()
            level += 1
            enemyX = 300
            EnemyY = 0
            chargeLevel = 1
            textDisplay = True
            hasCoin = False
            enemyDead = False
            enemyHealth = level - 1
        elif level == 2:
            for i in range(9000):
                screen.fill(black)
                screen.blit(endLabelB, (100,(windowSize[1] /2)))
                screen.blit(endLabel2A, (100,windowSize[1] /2-100))
                pg.display.flip()
            level += 1
            chargeLevel = 2
            textDisplay = True
            hasCoin = False
            enemyDead = False
            enemyHealth = level - 1 
        elif level == 3:
            for i in range(9000):
                screen.fill(black)
                screen.blit(endLabelB, (100,(windowSize[1] /2)))
                screen.blit(endLabel3A, (100,windowSize[1] /2-100))
                pg.display.flip()
            level += 1
            chargeLevel = 3
            textDisplay = True
            hasCoin = False
            enemyDead = False
            enemyHealth = level - 1
        elif level == 4:
            for i in range(9000):
                screen.fill(black)
                screen.blit(endLabelB, (100,(windowSize[1] /2)))
                screen.blit(endLabel4A, (100,windowSize[1] /2-100))
                pg.display.flip()
            level += 1
            chargeLevel = 4
            textDisplay = True
            hasCoin = False
            enemyDead = False
            enemyHealth = level - 1
        elif level == 5:
            for i in range(9000):
                screen.fill(black)
                screen.blit(endLabelB, (100,(windowSize[1] /2)))
                screen.blit(endLabel5A, (100,windowSize[1] /2-100))
                pg.display.flip()
            level += 1
            chargeLevel = 5
            textDisplay = True
            hasCoin = False
            enemyDead = False
            enemyHealth = level-1
            
            
    if playerLife == 0:
        for i in range(9000):
            screen.fill(black)
            screen.blit(deathLabel, (100,(windowSize[1] /2)))
            pg.display.flip()
        playerLife = 3
        level = 1
        enemyHealth = level - 1
        enemyX = 0
        chargeLevel = 0
        #enemyY = random.randint(200,350)
        #enemyX = random .randint(0,windowSize[0])
    clock.tick(gameSpeed)
    pg.display.flip()
pg.quit()






"""NOTES/IDEAS
    have a charge bar: as the game goes on you need more or less coins to
    activate your powers.maybe 5-level coins to trigger hasCoin to be true

    

    
"""
