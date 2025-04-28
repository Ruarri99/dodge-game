import pygame
from common import *

class Life():
	def __init__(self, random_handler, display):
		self.random_handler = random_handler
		self.display_size = display.get_size()
		self.image = pygame.image.load("sprites\\heart_sprite.png").convert_alpha()
		self.size = (50, 50)
		self.pos = (self.random_handler.seedInt(0, self.display_size[0]-self.size[0]), 0-self.size[1])


	def draw(self, display):
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
		display.blit(self.image, self.rect)


	def move(self, y):
		self.pos = (self.pos[0], self.pos[1]+y)


	def getPos(self):
		return self.pos
		

	def getSize(self):
		return self.size


class Points():
	def __init__(self, random_handler, display):
		self.random_handler = random_handler
		self.display_size = display.get_size()
		self.image = pygame.image.load("sprites\\coin_sprite.png").convert_alpha()
		self.size = (50, 50)
		self.pos = (self.random_handler.seedInt(0, self.display_size[0]-self.size[0]), 0-self.size[1])


	def draw(self, display):
		self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
		display.blit(self.image, self.rect)


	def move(self, y):
		self.pos = (self.pos[0], self.pos[1]+y)


	def getPos(self):
		return self.pos
		

	def getSize(self):
		return self.size