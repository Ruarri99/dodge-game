import pygame
from common import *
from menus.menu_base import MenuBase

class MainMenu(MenuBase):
    def __init__(self, display, manager):
        super().__init__(display, manager)

        self.local_game_button = Button("Local", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2-60, 200, 50), self.startLocalGame)
        self.credits_button = Button("Credits", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2, 200, 50), self.creditsMenu)
        self.quit_button = Button("Quit", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2+60, 200, 50), self.quitGame)


    def handleEvents(self, events):
        self.next_menu = None

        for event in events:
            self.local_game_button.handleEvent(event)
            self.credits_button.handleEvent(event)
            self.quit_button.handleEvent(event)

        return self.next_menu


    def draw(self):
        self.display.fill(COLOURS["WHITE"])
        self.local_game_button.draw(self.display)
        self.credits_button.draw(self.display)
        self.quit_button.draw(self.display)


    def startLocalGame(self):
        self.next_menu = "local_game"


    def creditsMenu(self):
        self.next_menu = "credits"


    def quitGame(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))