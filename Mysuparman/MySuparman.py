import pygame
try:
    import pkg_resources.py2_warn
    
except ImportError:
    pass

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Supar Man')
over = False

fullmone = pygame.image.load("assets/fullmone.jpeg")
fullmone = pygame.transform.scale(fullmone, (800, 600))

img = pygame.image.load("assets/buildings.png")
img = pygame.transform.scale(img, (800, 600))


ring = pygame.image.load("assets/ring.png")
ring = pygame.transform.scale(ring, (200, 150))

helth = pygame.image.load("assets/helth.png")
helth = pygame.transform.scale(helth, (50, 50))

suparman = pygame.image.load("assets/suparman.png")
suparman = pygame.transform.scale(suparman, (200, 200))
suparman = pygame.transform.flip(suparman, True, False)

pygame.mixer.music.load('assets/Honaa.wav')
pygame.mixer.music.play(-1)


clock = pygame.time.Clock()
mr = 0
nmr = -800

skay1 = 0
skay2 = 800
score = 0
overfalg = False
x = 0
y = 50
newx = 0
newy = 0
helthpoint = 3
valume = 0.5

font_style = pygame.font.SysFont("Arial", 30)


def message(msg, color, w, h):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w/3, h/3])


def moveseen(mr, nmr):
    mr += 5
    nmr += 5

    if mr >= 800:
        print("image 1 end")
        mr = -800
    if nmr >= 800:
        print("image2 end")
        nmr = -800

    return mr, nmr


while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                newy = -4

            if event.key == pygame.K_DOWN:

                newy = 4
            if event.key == pygame.K_m:
                print("stop music")
            if event.key == pygame.K_1:
                if valume <=1:
                    valume += 0.1
            if event.key == pygame.K_2:
                if valume >=0.0:
                    valume -= 0.1
    pygame.mixer.music.set_volume(valume)
    y += newy

    if y >= 450 or y <= -20:
        helthpoint -= 1

        if helthpoint == 0:
            overfalg = True

    mr, nmr = moveseen(mr, nmr)
    
   

    dis.blit(fullmone, (0, 0))
    dis.blit(img, (mr, 0))
    dis.blit(img, (nmr, 0))

    dis.blit(ring, (300, -70))
    dis.blit(ring, (400, -70))
    dis.blit(ring, (200, -70))

    dis.blit(ring, (300, 500))
    dis.blit(ring, (400, 500))
    dis.blit(ring, (200, 500))

    dis.blit(suparman, (350, y))
    #helth
    w = 600
    for i in range(helthpoint):
        
        dis.blit(helth,(w,0))
        w += 50
   

    message("1:volume ++",(255,255,255),0,0)
    message("2:volume --",(255,255,255),0,100)
    message("Score:", (255, 255, 51), 0, 200)
    score += 1
    message(str(score), (255, 255, 255), 300, 200)

    
        


    if overfalg:
	    # pygame.time.delay(50)
        message("Game Over", (255, 0, 0), 400, 300)
        pygame.time.wait(100)

       
        over = True


    pygame.display.update()

    dis.fill([255, 255, 255])
    clock.tick(30)


pygame.quit()
quit()
