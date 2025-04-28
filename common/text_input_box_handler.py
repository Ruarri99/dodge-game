from common.text_handler import *

class TextInputBox:
    def __init__(self, pos, size, colour_active=COLOURS["BLACK"], colour_inactive=COLOURS["GREY"], font_size=20, limit=None):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color_inactive = colour_inactive
        self.color_active = colour_active
        self.color = self.color_inactive
        self.text = Text("", (self.rect.x + 5, self.rect.y + 5), align="topleft")
        self.limit = limit
        self.active = False


    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text.setText(self.text.getText()[:-1])
            elif event.unicode.isnumeric() and len(self.text.getText()) < (self.limit if self.limit != None else 9999999):
                self.text.setText(self.text.getText() + event.unicode)


    def draw(self, display):
        self.text.draw(display)
        pygame.draw.rect(display, self.color, self.rect, 2)


    def getInput(self):
        return self.text.getText()
