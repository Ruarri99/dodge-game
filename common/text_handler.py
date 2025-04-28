import pygame
from .constants import *

class Text():
	def __init__(self, text, pos, font="arialblack", font_size=20, text_colour=COLOURS["BLACK"], bg_colour=None, align="center"):
		self.text = text
		self.x = pos[0]
		self.y = pos[1]
		self.text_colour = text_colour
		self.bg_colour = bg_colour
		self.align = align

		self.setFont(font, font_size)
		self.renderText()


	def renderText(self):
		self.text_render = self.font.render(self.text, True, self.text_colour, self.bg_colour)
		self.text_rect = self.text_render.get_rect(**{self.align: (self.x, self.y)})


	def draw(self, display):
		display.blit(self.text_render, self.text_rect)


	def getText(self):
		return self.text


	def setText(self, text):
		self.text = text
		self.renderText()


	def setFont(self, font, font_size):
		self.font = pygame.font.SysFont(font, font_size)


	def setPos(self, pos):
		self.x = pos[0]
		self.y = pos[1]

		self.renderText()