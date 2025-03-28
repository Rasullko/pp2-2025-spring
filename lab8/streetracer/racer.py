import pygame, sys
import random, time
pygame.init()

font = pygame.font.SysFont("stcingkai", 60)
font_small = pygame.font.SysFont("stcingkai", 20)
game_over = font.render("Game Over", True, (255, 255, 255))

background = pygame.image.load("lab8/streetracer/AnimatedStreet.png")

clock = pygame.time.Clock()
speed = 5
coin_score = 0

screen = pygame.display.set_mode((400, 600))
screen.fill((255, 255, 255))
pygame.display.set_caption("eron don don")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/streetracer/steve.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 500)

    def move(self):
        press = pygame.key.get_pressed()
        if self.rect.left > 0:
            if press[pygame.K_a]:
                self.rect.move_ip(-5, 0)
        
        if self.rect.right < 400:
            if press[pygame.K_d]:
                self.rect.move_ip(5, 0)
            
        if self.rect.top > 0:
            if press[pygame.K_w]:
                self.rect.move_ip(0, -5)

        if self.rect.bottom < 600:
            if press[pygame.K_s]:
                self.rect.move_ip(0, 5)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/streetracer/Enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), random.randint(-100, -40))
 

    
    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/streetracer/diamond.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

    def add(self):
        self.rect.center = (random.randint(40, 360), 0)

p = Player()
e = Enemy()
c = Coin()

enemies = pygame.sprite.Group()
enemies.add(e)
coins = pygame.sprite.Group()
coins.add(c)
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)
all_sprites.add(c)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.7

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(coin_score), True, (0, 0, 0))
    sss = font_small.render("Your Score: ", True, (0, 0, 0))
    screen.blit(sss, (10, 10))
    screen.blit(scores, (90, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(p, coins):
        coin_score += 1
        pygame.display.update()
        c.add()
        

    if pygame.sprite.spritecollideany(p, enemies):
     screen.fill((0, 0, 0))
     screen.blit(game_over, (80, 250))
     pygame.display.update()
     for entity in all_sprites:
        entity.kill()
     time.sleep(2)
     pygame.quit()
     sys.exit()



    pygame.display.update()
    clock.tick(60)