import random

class Seed():
	def __init__(self, seed=None):
		self.seed = seed if seed != None else random.randint(0, 9999999)
		random.seed(self.seed)

	def getSeed(self):
		return self.seed


	def seedInt(self, i, j):
		return random.randint(i, j)


	def seedChoice(self, choiceList, weights=None):
		return random.choices(choiceList, weights=weights)[0]