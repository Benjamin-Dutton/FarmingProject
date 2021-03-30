import requests
from random import randint

def fetch_cost(itemid):
	'''pulls the cost from the api'''
	try:
		r = requests.get(f'https://services.runescape.com/m=itemdb_oldschool/api/graph/{itemid}.json')
		response = r.json()
		list_reponse = list(response['average'].values())
		return list_reponse[-1]
	except:
		return 0

class Trees():
	'''a class to define tree attributes'''
	def __init__(self,tree_name, exp, levelreq, itemid,growth_time=1, growth_chance=100, patches = 1):
		self.tree_name = tree_name
		self.exp = exp
		self.levelreq= levelreq
		self.growth_time = growth_time
		self.growth_chance = growth_chance
		self.patches = patches
		self.exp = exp
		self.cost = fetch_cost(itemid)
		self.gpgain = 0 


	def grow_patches (self, current_level):
		'''simulates the growth of trees'''
		total_exp = 0
		gpgained = 0
		if current_level >= self.levelreq:
			if self.growth_chance == 100:
				for i in range(self.patches):
					total_exp += self.exp
			else:
				for i in range(self.patches):
					growth_check = randint(1, 100)
					if growth_check <= self.growth_chance:
						total_exp += self.exp
						gpgained += self.gpgain

		cost_of_patches = (self.cost * self.patches) - gpgained
		return (total_exp, cost_of_patches)

	def update_gpgain(self, itemid, amount):
		'''Updates the estimated return on a sucessfully grown plant
		if gathered'''
		produce_value = fetch_cost(itemid)
		self.gpgain = produce_value * amount










