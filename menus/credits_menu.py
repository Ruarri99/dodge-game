import pygame
from common import *
from menus.menu_base import MenuBase

class CreditsMenu(MenuBase):
    def __init__(self, display, manager):
        super().__init__(display, manager)

        self.title_credit = Text("Credits:", (self.display.get_size()[0]//2, self.display.get_size()[1]//2-150), font_size=30)
        self.dev_credit = Text("Developed by: Ruarri Schoeman", (self.display.get_size()[0]//2, self.display.get_size()[1]//2-60))
        self.car_credit = Text("Car designed by macrovector / Freepik.com", (self.display.get_size()[0]//2, self.display.get_size()[1]//2))
        self.log_credit = Text("Log designed by brgfx / Freepik.com", (self.display.get_size()[0]//2, self.display.get_size()[1]//2+30))
        self.wall_credit = Text("Wall designed by valadzionak_volha / Freepik.com", (self.display.get_size()[0]//2, self.display.get_size()[1]//2+60))
        self.heart_credit = Text("Heart designed by juicy_fish / Freepik.com", (self.display.get_size()[0]//2, self.display.get_size()[1]//2+90))
        self.coin_credit = Text("Coin designed by freepik / Freepik.com", (self.display.get_size()[0]//2, self.display.get_size()[1]//2+120))
        self.back_button = Button("Back", (self.display.get_size()[0]//2-100, self.display.get_size()[1]//2+180, 200, 50), self.backButton)

        self.credits = [self.title_credit, self.dev_credit, self.car_credit, self.log_credit, self.wall_credit, self.heart_credit, self.coin_credit]


    def handleEvents(self, events):
        self.next_menu = None

        for event in events:
            self.back_button.handleEvent(event)

        return self.next_menu


    def draw(self):
        self.display.fill(COLOURS["WHITE"])
        self.back_button.draw(self.display)

        for credit in self.credits:
            credit.draw(self.display)


    def backButton(self):
        self.next_menu = "main"