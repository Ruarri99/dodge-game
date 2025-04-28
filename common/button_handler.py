from .text_handler import *
from .constants import *

class Button:
    def __init__(self, text, rect, callback=None, bg_colour=COLOURS["GREEN"], hover_colour=None, select_colour=None, font="arialblack", font_size=20, text_colour=COLOURS["BLACK"]):
        self.rect = pygame.Rect(rect)
        self.text = Text(text, self.rect.center, font=font, font_size=font_size, text_colour=text_colour)
        self.callback = callback
        self.bg_colour = bg_colour
        self.hover_colour = self._calculateHoverColour() if hover_colour == None else hover_colour
        self.select_colour = self._calculateSelectColour() if select_colour == None else select_colour
        self.selected = False
        self.hovered = False


    def handleEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and event.button == 1:
                if callable(self.callback):
                    self.callback()
                return True
        
        return False


    def draw(self, display):
        color = self.hover_colour if self.hovered else (self.select_colour if self.selected else self.bg_colour)
        pygame.draw.rect(display, color, self.rect, border_radius=8)
        self.text.draw(display)


    def setSelected(self, selected):
        self.selected = selected


    def _calculateHoverColour(self):
        r, g, b = self.bg_colour
        factor = 0.4
        r = int(r + (255 - r) * factor)
        g = int(g + (255 - g) * factor)
        b = int(b + (255 - b) * factor)
        return (r, g, b)


    def _calculateSelectColour(self):
        r, g, b = self.bg_colour
        factor = 0.7
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        return (r, g, b)
