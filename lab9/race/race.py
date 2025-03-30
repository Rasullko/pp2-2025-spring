import pygame, sys #pygame - библиотека для функций чтобы игры делать, sys - для функций связанные с самим компом.
import random, time
pygame.init() #запускать пайгейм библиотеку

font = pygame.font.SysFont("stcingkai", 60) #шрифт и размер для надписи          stcingkai - название шрифта
font_small = pygame.font.SysFont("stcingkai", 20) #то же самое
game_over = font.render("Game Over", True, (255, 255, 255)) #чтобы вывести на экран надпись (сама надпись, тру/фолс, цвет)

background = pygame.image.load("lab9/race/AnimatedStreet.png") #задний фон для игры

clock = pygame.time.Clock() #для фпс - кадры в секунду
speed = 5 #изначальная скорость
coin_score = 0 #изначальный скор

screen = pygame.display.set_mode((400, 600)) #размеры игрового поля/окна
screen.fill((255, 255, 255)) #заполнить экран цветом (255, 255, 255) - белый
pygame.display.set_caption("eron don don") #дать название для экрана (optional)

class Player(pygame.sprite.Sprite): #класс игрока, спрайт - взаимодействуемый предмет, класс - связь всяких функций и переменных под одно имя
    def __init__(self): #создание и вывод нашей машинки на экран
        super().__init__() #inheritance (чтобы функции и переменные были индивидуальны для этого класса)
        self.image = pygame.image.load("lab9/race/steve.png") #загрузка картинки с компа
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect() #создать взаимодействуемый прямоугольник вокруг картинки
        self.rect.center = (160, 500) #координаты появления персонажа

    def move(self): #функция чтобы персонаж двигался
        press = pygame.key.get_pressed() #чекать, нажата ли кнопка
        if self.rect.left > 0: #если левая часть перса НЕ прижата к левому краю окна:
            if press[pygame.K_a]: #и при этом мы жмем кнопку "а" английскую
                self.rect.move_ip(-5, 0) #то наш персонаж двигается на -5 координат по х и 0 по у(то есть движется в лево на 5)
        
        if self.rect.right < 400: #если правая часть персонажа НЕ прижата к правому краю окна:
            if press[pygame.K_d]: #и при этом мы жмем кнопку "d":
                self.rect.move_ip(5, 0) #то персонаж двигается на 5 координат по х и 0 по у(то есть движется в право на 5)
            
        if self.rect.top > 0: #если голова персонажа  НЕ прижата к верхушке окна:
            if press[pygame.K_w]: #и при этом мы жмем кнопку "w":
                self.rect.move_ip(0, -5) #то перс двигается на 0 по х и -5 по у(то есть движется вверх на 5)

        if self.rect.bottom < 600: #если низ персонажа НЕ прижат ко дну окна:
            if press[pygame.K_s]: #и при этом мы жмем кнопку "s":
                self.rect.move_ip(0, 5) #то персонаж двигается на 0 по х и 5 по у(то есть движется вниз на 5)

class Enemy(pygame.sprite.Sprite): #класс врагов (зомби)
    def __init__(self): #тут то же самое как у плейера
        super().__init__()
        self.image = pygame.image.load("lab9/race/Enemy.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0) #тут враг должен появляться на рандомной х координате (рандом числа от 40 до 360), и наверху окна (0 по у)
    
    def move(self):
        self.rect.move_ip(0, speed) #чтобы зомби двигались 0 по х (то есть тупо вниз) и speed по у (speed изначально 5, как мы писали раньше, но она будет увеличиваться)
        if (self.rect.top > 600): #если верхушка зомби коснулась дна окна:
            self.rect.top = 0 #то спавним ее на верху окна по у
            self.rect.center = (random.randint(40, 360), 0) #и на рандомной точке по х

class Coin(pygame.sprite.Sprite): #класс эмеральдов
    def __init__(self): #тут так же как у и врагов по сути
        super().__init__()
        self.image = pygame.image.load("lab9/race/emerald.png")
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

class SuperCoin(pygame.sprite.Sprite): #класс алмазов, точно так же как и изумруды
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab9/race/diamond.png")
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

p = Player() #создаем переменные и даем им функции классов чтобы ими можно было взаимодействовать
e = Enemy()
c = Coin()
sc = SuperCoin()

enemies = pygame.sprite.Group() #создаем группы спрайтов врагов чтобы было легче управлять ими всеми 
enemies.add(e) #добавляем переменную врага в группу всех врагов
coins = pygame.sprite.Group() #то же самое с богатствами
coins.add(c)
scc = pygame.sprite.Group() #и суперкойнами (алмазы)
scc.add(sc)
all_sprites = pygame.sprite.Group() #группа всех спрайтов (койны, враги, плейер)
all_sprites.add(p)
all_sprites.add(e)
all_sprites.add(c)
all_sprites.add(sc)

INC_SPEED = pygame.USEREVENT + 1 #USEREVENT чтобы свои функции добавить в пайгейм
pygame.time.set_timer(INC_SPEED, 2000) #таймер чтобы каждые 2000мс = 2 секунды добавлять скорость 

while True: #бесконечный луп, чтобы игра продолжалась пока машины не ударились
    for event in pygame.event.get(): #луп пробегается по всем функциям пайгейма
        if event.type == INC_SPEED: #и если включилась функция INC_SPEED, которую мы сами написали, то:
            speed += 0.7 #то увеличиваем изначальную скорость(которая была равна 5) на 0.7

        if event.type == pygame.QUIT: #если нажали на крестик, то:
            pygame.quit() #заканчивается игра
            sys.exit() #и закрывается окно

    screen.blit(background, (0, 0)) #вставляет нашу background картинку на задний фон на координаты (0, 0)  
    scores = font_small.render(str(coin_score), True, (0, 0, 0)) #переменная чтобы  на экран наш скор в черном цвете (0, 0, 0)
    sss = font_small.render("Your Score: ", True, (0, 0, 0)) #выводит надпись Your Score: на экран 
    screen.blit(sss, (10, 10)) #blit - чтобы выводить на экран
    screen.blit(scores, (90, 10))

    for entity in all_sprites: #создаем луп чтобы пробегаться по группе всех спрайтов
        screen.blit(entity.image, entity.rect) #каждого выводим на экран
        entity.move() #и заставляем их двигаться

    if pygame.sprite.spritecollideany(p, coins): #spritecollideany - функция чтобы чекать если спрайты соприкоснулись. 
        coin_score += 1 #если плейер и группа обычных койнов соприкоснулись, то добавляем 1 к счету
        pygame.display.update() #обновляем дисплей чтобы убрать койн
        c.add() #создаем новый койн на экране, чтобы он появился наверху

    if pygame.sprite.spritecollideany(p, scc): #то же самое с суперкойнами
        coin_score += 5
        pygame.display.update()
        sc.add()
        

    if pygame.sprite.spritecollideany(p, enemies): #если плейер столкнется с группой врагов
        screen.fill((0, 0, 0)) #то закрашиваем фон черным
        screen.blit(game_over, (80, 250)) #выводим надпись геймовер в (80, 250) координатах
        pygame.display.update() #обновляем дисплей
        for entity in all_sprites:
            entity.kill() #убиваем (убираем с экрана) всех спрайтов
        time.sleep(2) #ждем две секунды
        pygame.quit() #и заканчиваем игру
        sys.exit() #и закрываем окно

    pygame.display.update() #обновляем дисплей
    clock.tick(60) #ставим фпс на 60 чтобы картинка была плавной