import pygame
pygame.init()
screen = pygame.display.set_mode((800, 700))
done = False
x = 25
y = 25
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    press = pygame.key.get_pressed()
    if press[pygame.K_w]: y -= 20
    if press[pygame.K_s]: y += 20
    if press[pygame.K_d]: x += 20
    if press[pygame.K_a]: x -= 20

    if x + 25 > 800:
        x = 775
    if x - 25 < 0:
        x = 25
    if y - 25 < 0:
        y = 25
    if y + 25 > 700:
        y = 675
    
    pygame.draw.circle(screen, (180, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(30)