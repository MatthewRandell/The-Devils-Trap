import pygame as pg
import ingamesprites as s

hasCoin = False
locked = False
runToggle = False
count = 0
windowSize = [600,600]
x = windowSize[0] / 2 -16
y = windowSize[1] / 2 -16

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

def Controlls():
    global hasCoin 
    global locked 
    global runToggle
    global y
    global x
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        if not hasCoin:
            image = move(s.sBack1,s.sBack2)
            currImg = s.sBack1
            y -= 1
        else:
            image = move(s.back1,s.back2)
            currImg = s.back1
            y -= 1
    elif keys[pg.K_d]:
        if not hasCoin:
            image = move(s.sRight1,s.sRight2)
            currImg = s.sRight2
            x += 1
        else:
            image = move(s.right1,s.right2)
            currImg = s.right2
            x += 1
    elif keys[pg.K_s]:
        if not hasCoin:
            image = move(s.sFront1,s.sFront2)
            currImg = s.sFront1
            y += 1
        else:
            image = move(s.front1,s.front2)
            currImg = s.front1
            y += 1
    elif keys[pg.K_a]:
        if not hasCoin:
            image = move(s.sLeft1,s.sLeft2)
            currImg = s.sLeft2
            x -= 1
        else:
            image = move(s.left1,s.left2)
            currImg = s.left2
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
        #image = currImg
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
                #locked = False
            
            count += 1

    
