import pygame
try:
    import pkg_resources.py2_warn
    
except ImportError:
    pass

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Supar Man')
over = False

fullmone = pygame.image.load("fullmone.jpeg")
fullmone = pygame.transform.scale(fullmone, (800, 600))

img = pygame.image.load("buildings.png")
img = pygame.transform.scale(img, (800, 600))


ring = pygame.image.load("ring.png")
ring = pygame.transform.scale(ring, (200, 150))
suparman = pygame.image.load("suparman.png")
suparman = pygame.transform.scale(suparman, (200, 200))
suparman = pygame.transform.flip(suparman, True, False)


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

font_style = pygame.font.SysFont(None, 40)


def message(msg, color, w, h):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w/3, h/3])


def moveseen(mr, nmr):
    mr += 3
    nmr += 3

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

                newy = -3

            if event.key == pygame.K_DOWN:

                newy = 3

    y += newy

    if y >= 450 or y <= -50:

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

    message("Score:", (0, 5, 255), 0, 100)
    score += 1
    message(str(score), (255, 255, 255), 300, 100)
    if overfalg:
        message("Game Over", (255, 0, 0), 400, 300)
        over = True

    pygame.display.update()

    dis.fill([255, 255, 255])
    clock.tick(60)


pygame.quit()
quit()
