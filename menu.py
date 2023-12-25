import pygame
from methods import visualizer


#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

# image class
class Image():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self, surface):
		# draw image on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))


def main_menu(window, width):


    title_img = pygame.image.load('title.png')
    start_img = pygame.image.load('start.png')

    title = Image(90, 90, title_img, 0.5)
    start_button = Button(width/2-140, width-300, start_img, 0.5)

    run = True
    while run:

        window.fill((255,255,255))

        title.draw(window)

        if start_button.draw(window):
            visualizer(window, width)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()