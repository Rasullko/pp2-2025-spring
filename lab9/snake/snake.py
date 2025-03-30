import pygame
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500  #размеры экрана
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # игровое окно
done = True

#цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)
time = 0

BLOCK_SIZE = 20  #размеры стороны блока в игре

clock = pygame.time.Clock()
FPS = 6                     #фпс для плавности игры (кадры в секунду)

def draw_grid():         #функция чтобы сделать фон в клетку
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):       #для х: с 0 до 500 пикселей и через каждые 20 пикселей(блок-сайз)
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):    # для у: с 0 до 500 пикселей и через каждые 20 пикселей(блок-сайз)
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)
  

class Wall:          #класс препятствий
  def __init__(self):
    self.body = []   #список для координат стенок
    self.load_wall()
  
  def load_wall(self):
    with open(f'lab9/snake/level1.txt', 'r') as f:   #открывает текстовый файл
      wall_body = f.readlines()           #и читает его
    
    for i, line in enumerate(wall_body): 
      for j, value in enumerate(line):
        if value == '#':                  #пробегается по файлу и каждый символ # заменяет стенкой (препятствием)
          self.body.append([j, i])
  
  def draw(self): 
    for x, y in self.body:                #выводит все препятствия на экран
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

class Point:
  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = Point(self.x, self.y)
        
    def draw(self):
        point = self.location
        pygame.draw.rect(screen, RED, (point.x * BLOCK_SIZE, point.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        
    
class Food:                         #класс еды
  def __init__(self):

      self.generate_random_pos()    #функция чтобы генерировать случайные координаты для еды
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)
  
  def generate_random_pos(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))

  def respawn(self):                #функция чтобы выводить на экран новый блок еды
    self.generate_random_pos()   
  
  def draw(self):                   #выводить на экран
    pygame.draw.rect(screen, BLUE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


class Snake:
  def __init__(self):
      self.body = [[10, 10], [11, 10],]       #начальные координаты змейки
      self.dx = 1                            #скорость по х
      self.dy = 0                            #скорость по у
  
  def draw(self):
    for i, (x, y) in enumerate(self.body):   
      color = WHITE if i == 0 else GREEN       #чтобы голлова была белой, а тело зеленое
      pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1): # добавление блока в тело змейки 
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx       # двигаем постоянно
    self.body[0][1] += self.dy       # двигаем постоянно

    #чтобы змея проходила скозь экран и выходила с противополжной стороны
    if self.body[0][0] * BLOCK_SIZE > WINDOW_WIDTH:    
            self.body[0][0] = 0
        
    if self.body[0][1] * BLOCK_SIZE > WINDOW_HEIGHT:
          self.body[0][1] = 0

    if self.body[0][0]< 0:
        self.body[0][0] = WINDOW_WIDTH / BLOCK_SIZE
    
    if self.body[0][1] < 0:
        self.body[0][1] =WINDOW_HEIGHT/ BLOCK_SIZE
  

snake = Snake()  #создаем саму змейку и добавляем ее в класс Snake
food = Food()
wall = Wall()
block = Block(0, 0)
level = 1
score = 0

while done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      done = False

    #движение змейки соответсвенно кнопкам
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        snake.dx = 1
        snake.dy = 0
      if event.key == pygame.K_LEFT:
        snake.dx = -1
        snake.dy = 0
      if event.key == pygame.K_UP:
        snake.dx = 0
        snake.dy = -1
      if event.key == pygame.K_DOWN:
        snake.dx = 0
        snake.dy = 1
      if event.key == pygame.K_SPACE:
        pass 
  
  #добавляем стенки в запущенную игру
  wallsCoor = open(f"lab8/snake/level1.txt", 'r').readlines()
  walls = []
  for i, line in enumerate(wallsCoor):
      for j, each in enumerate(line):
          if each == "#":
            walls.append(Block(j, i))  
  
  #когда змейка сталкивается с препядствием, игра завершается
  for block in walls:
    block.draw()
    if snake.body[0][0] == block.x and snake.body[0][1] == block.y:
      done = False    
  
  #включаем ранее написанные функции
  snake.move()    
    
  screen.fill(BLACK)
  
  draw_grid()
  snake.draw()
  food.draw()
  wall.draw()

  #если змейка дойдет до еды, она появляется в новом месте
  if food.x == block.x and food.y == block.y:
    food.respawn()
  
  #увеличивается длинна змейки и увеличивается счет при столкновении с едой
  if snake.body[0][0] * BLOCK_SIZE == food.x and snake.body[0][1] * BLOCK_SIZE == food.y:
    snake.body.append([0, 0])
    food.generate_random_pos()
    score += random.randint(1, 3)
    #переход на новый уровень и увеличение скорости змейки
    if score%5==0 and score!=0:
      FPS +=4
      level+=1

  #еда появляется на новом месте если не успел взять ее вовремя
  time += FPS % 4
  if time % 100 == 0 and time != 0:
    food.respawn()

  #счетчик и уровень
  font = pygame.font.Font(None, 30)
  text = font.render(f'Score: {score}', True, (255, 0, 0))
  font_l = pygame.font.Font(None, 30)
  levell = font_l.render("LEVEL:"+str(level), True, (WHITE))
  screen.blit(levell, (300,20))
  screen.blit(text, (20, 20))
  
  pygame.display.update()
  clock.tick(FPS)