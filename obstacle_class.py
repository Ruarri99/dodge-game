import pygame
from common import *

class Tree():
	def __init__(self, random_handler, display):
		self.random_handler = random_handler
		self.display_size = display.get_size()
		self.image = pygame.image.load("sprites\\tree_sprite.png").convert_alpha()
		self.size = (50, 100)
		self.pos = (self.random_handler.seedInt(0, self.display_size[0]-self.size[0]), 0-self.size[1])
		

	def draw(self, display):
		self.rect = self.image.get_rect(midbottom=(self.pos[0]+self.size[0]//2, self.pos[1]+self.size[1]))
		display.blit(self.image, self.rect)


	def move(self, y):
		self.pos = (self.pos[0], self.pos[1]+y)


	def getPos(self):
		return self.pos
		

	def getSize(self):
		return self.size



class Wall():
	def __init__(self, random_handler, display):
		self.random_handler = random_handler
		self.display_size = display.get_size()
		self.image = pygame.image.load("sprites\\wall_sprite.png").convert_alpha()
		self.size = (200, 50)
		self.pos = (self.random_handler.seedInt(0, self.display_size[0]-self.size[0]), 0-self.size[1])


	def draw(self, display):
		self.rect = self.image.get_rect(bottomleft=(self.pos[0], self.pos[1]+self.size[1]))
		display.blit(self.image, self.rect)


	def move(self, y):
		self.pos = (self.pos[0], self.pos[1]+y)


	def getPos(self):
		return self.pos
		

	def getSize(self):
		return self.size