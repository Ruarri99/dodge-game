from common.button_handler import Button
from common.constants import *

class RadioSelection():
	def __init__(self, pos, size, button_labels, padding=10, font_size=20, bg_colour=COLOURS["GREEN"], text_colour=COLOURS["BLACK"]):
		self.pos = pos
		self.size = size
		self.padding = padding
		self.selected = 0
		self.button_labels = button_labels
		self.buttons = []
		self.font_size = font_size
		self.bg_colour = bg_colour
		self.text_colour = text_colour

		self._generateButtons()


	def handleEvent(self, event):
		for i, button in enumerate(self.buttons):
			if button.handleEvent(event):
				self.selected = i

		for i, button in enumerate(self.buttons):
			button.setSelected(i == self.selected)


	def draw(self, display):
		for button in self.buttons:
			button.draw(display)


	def getSelected(self):
		return self.selected


	def _generateButtons(self):
		count = len(self.button_labels)
		total_width = count * self.size[0] + (count - 1) * self.padding
		start_x = self.pos[0] - total_width / 2
		rect_y = self.pos[1] - self.size[1] / 2

		for i, button in enumerate(self.button_labels):
			rect_x = start_x + i * (self.size[0] + self.padding)
			self.buttons.append(Button(button, (rect_x, rect_y, self.size[0], self.size[1]), font_size=self.font_size, bg_colour=self.bg_colour, text_colour=self.text_colour))


