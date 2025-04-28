import pygame
from common import *
from menus.menu_base import MenuBase

class EndGameMenu(MenuBase):
	def __init__(self, display, manager, players, obstacle_count, random_handler):
		super().__init__(display, manager)
		
		self.players = players
		self.obstacle_count = obstacle_count
		self.random_handler = random_handler
		self.score_texts = []

		for i, player in enumerate(self.players):
			self.score_texts.append(Text(f"Player {i+1}: {player.getScore()}", (self.display.get_size()[0]//2, self.display.get_size()[1]//2-60*len(self.players)+i*60)))

		self.obstacle_count_text = Text(f"Obstacle Count: {self.obstacle_count}", (self.display.get_size()[0]//2, self.display.get_size()[1]//2))
		self.seed_text = Text(f"Seed: {self.random_handler.getSeed()}", (self.display.get_size()[0]//2, self.display.get_size()[1]//2+60))
		self.main_menu_button = Button("Main Menu", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2+120, 200, 50), self.gotoMainMenu)


	def handleEvents(self, events):
		self.next_menu = None
		for event in events:
			self.main_menu_button.handleEvent(event)

		return self.next_menu


	def draw(self):
		self.display.fill(COLOURS["WHITE"])

		for score_text in self.score_texts:
			score_text.draw(self.display)

		self.obstacle_count_text.draw(self.display)
		self.seed_text.draw(self.display)
		self.main_menu_button.draw(self.display)


	def gotoMainMenu(self):
		self.next_menu = "main"