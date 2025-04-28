import pygame
import time
import obstacle_class
import powerup_class
from common import *
from menus.menu_base import MenuBase

class LocalGameplay(MenuBase):
	def __init__(self, display, manager, players, random_handler):
		super().__init__(display, manager)

		self.players = players
		self.player_texts = []
		self.player_score_texts = []
		self.player_life_texts = []
		self.random_handler = random_handler
		self.running = True
		self.obstacles = []
		self.obstacle_count = 1
		self.obstacle_frame_count = 0
		self.obstacle_frame_total = 1000
		self.powerups = []
		self.powerup_frame_count = 0
		self.powerup_frame_total = 1000
		self.obstacle_count_text = Text(f"Obstacles: {self.obstacle_count}", (self.display.get_size()[0], 0), font_size=20, align="topright")
		self.countdown_length = 3
		self.countdown_count = 3
		self.countdown_text = Text(f"Starting in {self.countdown_count}...", (self.display.get_size()[0]//2, self.display.get_size()[1]//2), font_size=30)
		self.countdown_start_time = pygame.time.get_ticks()
		self.blink_speed = 100
		self.blink_timer = pygame.USEREVENT + 1
		self.ghost_length = 3000
		self.coin_collect_text = Text(f"+500", (0, 0), font_size=15)
		self.coin_collect_text_length = 2000
		self.coin_collect_time = 0

		pygame.time.set_timer(self.blink_timer, self.blink_speed)

		for i, player in enumerate(self.players):
			player.setPos(self.display.get_size()[0]//2 - player.getSize()[0]//2, self.display.get_size()[1] - player.getSize()[1])

			self.player_texts.append(Text(f"Player {i+1}", (0, 0+i*100), align="topleft"))
			self.player_life_texts.append(Text(f"Lives: {player.getLives()}", (0, 20+i*100), align="topleft"))
			self.player_score_texts.append(Text(f"Score: {player.getScore()}", (0, 40+i*100), align="topleft"))


	def handleEvents(self, events):
		if not self.running:
			pygame.time.set_timer(self.blink_timer, 0)
			time.sleep(2)
			return ("end_game", {
				"players": self.players,
				"obstacle_count": self.obstacle_count,
				"random_handler": self.random_handler
			})

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT]:
			self.players[0].move(-5)
		if pressed[pygame.K_RIGHT]:
			self.players[0].move(5)

		if len(self.players) == 2:
			if pressed[pygame.K_a]:
				self.players[1].move(-5)
			if pressed[pygame.K_d]:
				self.players[1].move(5)

		for event in events:
			if event.type == self.blink_timer:
				for player in self.players:
					if player.getGhost():
						if pygame.time.get_ticks() - player.getGhostStartTime() >= self.ghost_length:
							player.unGhost()
						else:
							player.blink()


	def update(self):
		if self.countdown_count > 0:
			seconds_passed = (pygame.time.get_ticks() - self.countdown_start_time)//1000
			self.countdown_count = self.countdown_length - seconds_passed
			self.countdown_text.setText(f"Starting in {self.countdown_count}...")
		else:
			self.obstacle_frame_count += 1
			if self.obstacle_frame_count > self.obstacle_frame_total:
				self.obstacle_frame_count = 0
				self.obstacle_count += 1

			self.powerup_frame_count += 1
			if self.powerup_frame_count > self.powerup_frame_total:
				self.powerup_frame_count = 0
				self.powerups.append(self.random_handler.seedChoice([powerup_class.Life(self.random_handler, self.display), powerup_class.Points(self.random_handler, self.display)], [40, 60]))

			if len(self.obstacles) < self.obstacle_count:
				self.obstacles.append(self.random_handler.seedChoice([obstacle_class.Tree(self.random_handler, self.display), obstacle_class.Wall(self.random_handler, self.display)]))

			for obs in self.obstacles:
				if obs.getPos()[1] > self.display.get_size()[1]:
					self.obstacles.remove(obs)
				else:
					obs.move(5)

				for player in self.players:
					if player.getDead() == False and player.getGhost() == False and pygame.Rect(player.getPos() + player.getSize()).colliderect(pygame.Rect(obs.getPos() + obs.getSize())):
						player.loseLife()
						if player.getLives() ==0:
							player.setDead(True)
						else:
							player.ghost()


			for power in self.powerups:
				if power.getPos()[1] > self.display.get_size()[1]:
					self.powerups.remove(power)
				else:
					power.move(5)

				for player in self.players:
					if pygame.Rect(player.getPos() + player.getSize()).colliderect(pygame.Rect(power.getPos() + power.getSize())):
						if isinstance(power, powerup_class.Life):
							player.gainLife()
							if player.getDead() == True:
								player.setDead(False)
								player.ghost()
						elif isinstance(power, powerup_class.Points):
							player.setScore(player.getScore()+500)
							self.coin_collect_text.setPos((power.getPos()[0]+power.getSize()[0]//2, power.getPos()[1]+power.getSize()[1]//2))
							self.coin_collect_time = pygame.time.get_ticks()

						self.powerups.remove(power)

			self.running = False
			for player in self.players:
				if player.getDead() == False:
					self.running = True

				if player.getDead() == False and player.getGhost() == False:
					player.setScore(player.getScore() + 1)


		for player in self.players:
			if player.getPos()[0] < 0:
				player.setPos(0, player.getPos()[1])
			elif player.getPos()[0]+player.getSize()[0] > self.display.get_size()[0]:
				player.setPos(self.display.get_size()[0]-player.getSize()[0], player.getPos()[1])

		for i, player_score_text in enumerate(self.player_score_texts):
			player_score_text.setText(f"Score: {self.players[i].getScore()}")

		for i, player_life_text in enumerate(self.player_life_texts):
			player_life_text.setText(f"Lives: {self.players[i].getLives()}")

		self.obstacle_count_text.setText(f"Obstacles: {self.obstacle_count}")


	def draw(self):
		self.display.fill(COLOURS["WHITE"])

		for obs in self.obstacles:
			obs.draw(self.display)

		for power in self.powerups:
			power.draw(self.display)

		for player in self.players:
			player.draw(self.display)

		for player_text in self.player_texts:
			player_text.draw(self.display)

		for player_score_text in self.player_score_texts:
		 	player_score_text.draw(self.display)

		for player_life_text in self.player_life_texts:
		 	player_life_text.draw(self.display)

		if pygame.time.get_ticks() < self.coin_collect_time + self.coin_collect_text_length:
			self.coin_collect_text.draw(self.display)


		self.obstacle_count_text.draw(self.display)

		if self.countdown_count > 0:
			self.countdown_text.draw(self.display)