import pygame
import random
pygame.init()

window = pygame.display.set_mode((402, 402))
pygame.display.set_caption("Zmey 3000")
screen = pygame.Surface((402, 402))
done = True #Для головного циклу
#Малюємо сітку
def drav_setka():
	x = 0
	x_x = 400
	y = 0
	y_y = 400
	for i in range(11):
		pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y_y), 2)
		x += 40
	x = 0
	for i2 in range(11):
		pygame.draw.line(screen, (255, 255, 255), (x, y), (x_x, y), 2)
		y += 40
#Клас героя, елемента хвоста, яблука
class Zmey():
	def _init_(self, xpos, ypos, filename):
		self.xpos = xpos
		self.ypos = ypos
		self.bitmap = pygame.image.load(filename)
	def render(self):
		screen.blit(self.bitmap, (self.xpos * 40 + 2, self.ypos *40 + 2))
#Рух хвоста
def going_hv():
	x = 2
	y = len(list)
	for i in reversed(list[1:]):
			i.xpos, i.ypos = list[y - x].xpos, list[y - x].ypos
			x += 1
#Для рахунку
counter = 0

hvost = Zmey(4, 5, 'element.jpg')
hero = Zmey(4, 4, 'element.jpg')
going = '' #Для клавіш
list [hero, hvost] #Тут зберігається змійка

#Рух хвоста змійки
def do_going(going):
	if going == 'left':
		going_hv()
		list[0].xpos -= 1
		if list[0].xpos < 0: 
			list[0].xpos = 9
	if going == 'right':
		going_hv()
		list[0].xpos += 1
		if list[0].xpos > 9: 
			list[0].xpos = 0		
	if going == 'up':
		going_hv()
		list[0].ypos -= 1
		if list[0].ypos < 0: 
			list[0].ypos = 9		
	if going == 'down':
		going_hv()
		list[0].ypos += 1
		if list[0].ypos > 9: 
			list[0].ypos = 0
apple = Zmey(10, 10, 'apple.png')

#Генерація яблука
def apple_gen(list):
	x = random.randint(0, 9)
	y = random.randint(0, 9)
	for i in list:
		if (i.xpos, i.ypos) == (x, y):
			x, y = apple_gen(list)
		else:
			continue
	return x, y
apple.xpos, apple.ypos = apple_gen(list) #Початкове положення яблука
while done:
	some_x = list[len(list) - 1].xpos #Якщо буде зїдено яблуко, добавленій частині хвоста передається це значення по Х	
	some_y = list[len(list) - 1].ypos #Якщо буде зїдено яблуко, добавленій частині хвоста передається це значення по Y	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = False
		if event.type == pygame.KEYDOWN:
			#Вияснюємо яка кнопка була нажата
			if event.key == pygame.K_LEFT:
				going = 'left'
			if event.key == pygame.K_RIGHT:
				going = 'right'
			if event.key == pygame.K_UP:
				going = 'up'
			if event.key == pygame.K_DOWN:
				going = 'down'
	do_going(going) #Передаємо нові координати змійки 
	#Якщо зїдено яблуко
	if list[0].xpos == apple.xpos and list[0].ypos == apple.ypos:
		counter += 1
		list.append(Zmey( some_x, some_y, 'element.jpg'))
		apple.xpos, apple.ypos = apple_gen(list)
	screen.fill((0, 0, 0))
	drav_setka()

	for i in list:
		i.render()
	apple.render()
	window.blit(screen, (0, 0))
	pygame.display.flip()
	pygame.time.delay(300)