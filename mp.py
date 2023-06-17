import pygame,sys,pymunk

def create_apple(space,pos):
	body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
	body.position = pos
	shape = pymunk.Circle(body,50)
	space.add(body,shape)
	return shape

def draw_apples(apples):
	for apple in apples:
		pos_x=int(apple.body.position.x)
		pos_y=int(apple.body.position.y)
		apple_rect=apple_surface.get_rect(center=(pos_x,pos_y))
		screen.blit(apple_surface,apple_rect)
		#pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),80)

def static_ball(space):
	body=pymunk.Body(body_type=pymunk.Body.STATIC)
	body.position=(800,800)
	shape=pymunk.Circle(body,50)
	space.add(body,shape)
	return shape

def draw_static_ball(balls):
	for ball in balls:
		pos_x=int(ball.body.position.x)
		pos_y=int(ball.body.position.y)
		pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50)


pygame.init()
screen=pygame.display.set_mode((80,80))
Clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,100)
apple_surface=pygame.image.load("apple2.png")
apples =[]
#apples.append(create_apple(space,pos))

balls=[]
balls.append(static_ball(space))




while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			apples.append(create_apple(space,event.pos))
	 
	screen.fill((200,200,200))
	draw_apples(apples)
	draw_static_ball(balls)
	space.step(1/50)
	pygame.display.update()
	Clock.tick(200)