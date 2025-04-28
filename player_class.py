import pygame

class Player():
	def __init__(self, image):
		self.image = pygame.image.load(f"sprites\\{image}.png").convert_alpha()
		self.blink_image = self._calculateBlinkImage()
		self.draw_image = self.image
		self.pos = (0, 0)
		self.size = (50, 100)
		self.score = 0
		self.lives = 3
		self.is_ghost = False
		self.ghost_start_time = 0
		self.dead = False


	def draw(self, display):
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
		if not self.dead:
			display.blit(self.draw_image, self.rect)
		else:
			display.blit(self.blink_image, self.rect)


	def setPos(self, x, y):
		self.pos = (x, y)


	def move(self, x):
		self.pos = (self.pos[0]+x, self.pos[1])


	def getPos(self):
		return self.pos
		

	def getSize(self):
		return self.size


	def setScore(self, score):
		self.score = score


	def getScore(self):
		return self.score


	def loseLife(self):
		self.lives -= 1


	def gainLife(self):
		self.lives += 1


	def getLives(self):
		return self.lives


	def blink(self):
		if self.draw_image == self.blink_image:
			self.draw_image = self.image
		else:
			self.draw_image = self.blink_image


	def ghost(self):
		self.is_ghost = True
		self.ghost_start_time = pygame.time.get_ticks()


	def unGhost(self):
		self.is_ghost = False
		self.draw_image = self.image
		self.ghost_start_time = 0


	def getGhost(self):
		return self.is_ghost


	def getGhostStartTime(self):
		return self.ghost_start_time


	def setDead(self, dead):
		self.dead = dead


	def getDead(self):
		return self.dead


	def _calculateBlinkImage(self):
		factor = 0.5
		image = self.image.copy()
		width, height = image.get_size()
		
		for x in range(width):
			for y in range(height):
				r, g, b, a = image.get_at((x, y))
				r = int(r + (255 - r) * factor)
				g = int(g + (255 - g) * factor)
				b = int(b + (255 - b) * factor)
				image.set_at((x, y), (r, g, b, a))
		
		return image