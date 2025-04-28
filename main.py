import pygame
import ctypes
import player_class
import obstacle_class
import seed_handler
from common import *
from menu_manager import MenuManager

def main():
	# ==== INITIALISATION ====

	# ~~ Pygame ~~

	try:
		ctypes.windll.user32.SetProcessDPIAware()
	except Exception:
		pass

	pygame.init()

	display_size = pygame.display.get_desktop_sizes()[0]
	display = pygame.display.set_mode((display_size[0], display_size[1]), pygame.FULLSCREEN)
	pygame.display.set_caption("Dodge Game")
	clock = pygame.time.Clock()


	# ~~ Menu ~~

	menu_manager = MenuManager(display)


	# ==== GAME LOOP ====


	running = True
	while running:

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				running = False

		menu_manager.handleEvents(events)
		menu_manager.update()
		menu_manager.draw()		

		pygame.display.update()
		clock.tick(240)


	pygame.quit()


if __name__ == "__main__":
	main()