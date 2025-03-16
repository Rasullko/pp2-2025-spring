import pygame 
import datetime
pygame.init()

screen = pygame.display.set_mode((1440, 1080))
bg = pygame.image.load('lab7/mickeybg.png')
sec = pygame.image.load('lab7/lefthand1.png')
min = pygame.image.load('lab7/righthand1.png')
pygame.display.set_caption("lab7/Mickey Clock")
sec=pygame.transform.scale(sec,(500,400))
min=pygame.transform.scale(min,(500,500))
clock = pygame.time.Clock() 
def Rotate(surf, image, topleft, angle): 
    rotated_image = pygame.transform.rotate(image, -1*angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect.topleft) 
 
done = False 
 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    clock.tick(60) 
    c = datetime.datetime.now() 
    seconds = c.second 
    minute = c.minute 
    
    angle_1 = (6 * seconds)
    angle_2 = (minute * 6 + ((seconds * 6) / 60))
    screen.blit(bg,(0,0)) 
    Rotate(screen, sec, (455,360), angle_1) 
    Rotate(screen, min, (455,300), angle_2)  
    pygame.display.flip() 
pygame.quit()