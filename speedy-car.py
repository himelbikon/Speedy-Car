import pygame, time, random, math

# variable area
display_width = 800
display_height = 600
FPS = 60
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
b_green = (0, 200, 0)
b_red = (200, 0, 0)
b_blue = (0, 0, 200)


# image area
load_car_img = pygame.image.load('f1.png')
car_img = pygame.transform.scale(load_car_img, (100, 100))


# game window area
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Speedy Car')
clock = pygame.time.Clock() 


# function area
def car(x, y):
	gameDisplay.blit(car_img, (x, y))

def obj(x, y, w, h, c):
	pygame.draw.rect(gameDisplay, c, [x, y, w, h])

def text_objects(text, font):
	textSur = font.render(text, True, black)
	return textSur, textSur.get_rect()

def scores(scr):
	s = 'Scores: ' + str(scr)
	font = pygame.font.Font('freesansbold.ttf', 15)
	text_surf, text_rect = text_objects(s, font)
	text_rect.center = (45, 15)
	gameDisplay.blit(text_surf, text_rect)

def msg_display(text):
	font = pygame.font.Font('freesansbold.ttf', 115)
	text_surf, text_rect = text_objects(text, font)
	text_rect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(text_surf, text_rect)
	pygame.display.update()
	time.sleep(2)
	game_loop()	

def crash():
	msg_display('You crashed!')

def cal_col(x, y, obj_x, obj_y):
	a = x - obj_x
	b = y - obj_y
	c = pow(a, 2) + pow(b, 2)
	res = math.sqrt(c)
	return res

def s_text(x, y, text):
	font = pygame.font.Font('freesansbold.ttf', 20)
	text_surf, text_rect = text_objects(text, font)
	text_rect.center = (x, y)
	gameDisplay.blit(text_surf, text_rect)

def game_intro():
	run = True
	while run:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		font = pygame.font.Font('freesansbold.ttf', 115)
		text_surf, text_rect = text_objects('Speedy Car', font)
		text_rect.center = ((display_width/2), ((display_height-100)/2))
		gameDisplay.blit(text_surf, text_rect)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if 150 < mouse[0] < 250 and 450 < mouse[1] < 500:
			pygame.draw.rect(gameDisplay, b_green,(150, 450, 100, 50))
			if click[0] == 1:
				game_loop()
		else:
			pygame.draw.rect(gameDisplay, green,(150, 450, 100, 50))

		if 550 < mouse[0] < 650 and 450 < mouse[1] < 500:
			pygame.draw.rect(gameDisplay, b_red, (550, 450, 100, 50))
			if click[0] == 1:
				pygame.quit()
				quit()	
		else:
			pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

		s_text(200, 475, 'Play')
		s_text(600, 475, 'Exit')

		pygame.display.update()
		clock.tick(60)


def game_loop():
	run = True
	x = display_width * 0.45
	y = display_height * 0.8
	vel = 5
	obj_y = -600
	obj_x = random.randrange(0, display_width)
	obj_w = 100
	obj_h = 100
	obj_c = black
	scr = 0
	obj_vel = 5


	while run:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		# movement
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			x += vel
		elif keys[pygame.K_LEFT]:
			x -= vel
		elif keys[pygame.K_UP] and y > 0:
			y -= vel
		elif keys[pygame.K_DOWN] and y < display_height -100:
			y += vel

		if x < 0 or x > display_width-100:
			#run = False
			crash()

		if obj_y > display_width:
			obj_y = -600
			obj_x = random.randrange(0, display_width)
			obj(obj_x, obj_y, obj_w, obj_h, obj_c)
			scr += 1
			obj_vel += 1

		#if abs(x - obj_x) <100 and abs(y - obj_y) < 100:
			#crash()

		if cal_col(x, y, obj_x, obj_y) < 100:
			crash()
		
		gameDisplay.fill(white)
		car(x, y)
		obj(obj_x, obj_y, obj_w, obj_h, obj_c)
		obj_y += obj_vel
		scores(scr)
		pygame.display.update() # blit() is same
		clock.tick(FPS) # FPS = 60

# main game area
game_intro()
game_loop()


# last area
pygame.quit()
quit()


