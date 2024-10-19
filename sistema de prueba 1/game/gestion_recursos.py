#from renpy.exports import notify

class PlayerResources: 
	def __init__(self):
		self.money = 100 #Dinero inicial
		self.energy = 100 #Energía inicial
		self.reputacion = 50 #Reputación inicial
		self.skills = {} #Habilidades iniciales

	def add_money(self,amount):
		self.money += amount
		return "Money increased by {}".format(amount)

	def spend_money(self, amount):
		if self.money >= amount:
			self.money -= amount
			return "Money spent: {}".format(amount)
		else: 
			return "Not enough money!"

	def gain_money(self, amount):
		self.energy += amount
		if self.energy > 100:
			self.energy = 100 #Definiendo la energía máxima.
		return "Energy increased by {}".format(amount) 

	def use_energy(self,amount):
		if self.energy >= amount: 
			self.energy -= amount
			return "Energy spent: {}".format(amount)
		else:
			return "Not enough energy!"

	def change_reputation(self,amount):
		self.reputacion += amount
		return "Reputation change by {}".format(amount) 

	def add_skill(self, skill_name, level):
		self.skills[skill_name] = level
		return "Skill {} added with level {}".format(skill_name) 

