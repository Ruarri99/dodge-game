import pygame
import seed_handler
import player_class
from common import *
from menus.menu_base import MenuBase


class LocalGameMenu(MenuBase):
    def __init__(self, display, manager):
        super().__init__(display, manager)

        self.playerSelector = RadioSelection((self.display.get_size()[0]//2, self.display.get_size()[1]//2-60), (100, 50), ["1 Player", "2 Players"], font_size=15, bg_colour=COLOURS["GREY"], text_colour=COLOURS["WHITE"])
        self.seed_text = Text("Seed: ", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2), align="midright")
        self.seed_text_input_box = TextInputBox((self.display.get_size()[0]//2-100, self.display.get_size()[1]//2-25), (200, 50), limit=7)
        self.play_button = Button("Play", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2+60, 200, 50), self.startGame)


    def handleEvents(self, events):
        self.next_menu = None
        for event in events:
            self.play_button.handleEvent(event)
            self.playerSelector.handleEvent(event)
            self.seed_text_input_box.handleEvent(event)

        return self.next_menu


    def draw(self):
        self.display.fill(COLOURS["WHITE"])
        self.play_button.draw(self.display)
        self.playerSelector.draw(self.display)
        self.seed_text.draw(self.display)
        self.seed_text_input_box.draw(self.display)


    def _initSeed(self):
        try:
            seed = int(self.seed_text_input_box.getInput())
        except Exception:
            seed = None

        return seed_handler.Seed(seed)


    def _initPlayers(self):

        players = []

        players.append(player_class.Player("red_car_sprite"))
        if self.playerSelector.getSelected() == 1:
            players.append(player_class.Player("blue_car_sprite"))

        return players


    def startGame(self):
        self.players = self._initPlayers()
        self.random_handler = self._initSeed()

        self.next_menu = ("local_gameplay", {
            "players": self.players,
            "random_handler": self.random_handler
        })