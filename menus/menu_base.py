import pygame

class MenuBase:
    def __init__(self, display, manager):
        self.display = display
        self.manager = manager


    def handle_events(self, events):
        pass


    def update(self):
        pass


    def draw(self):
        pass