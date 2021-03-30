from trees import Trees
from trees import fetch_cost

current_exp = 3762134
day = 0
levels = [3972294, 4385776, 4842295, 5346332, 5902831, 6517253, 7195629, 7944614,8771558, 9684577, 10692629,11805606,13034431]
cur_level = 86
day_level_gained = []
current_cost = 0
hespori = Trees('Hespori', 12600, 65,22875, growth_time=2)
fruit = Trees('Papaya', 6146.6, 57,5501 ,growth_chance=92, patches=6)
regular = Trees('Magic Tree',13919, 75,5374 ,patches = 6)
celastrus= Trees ('Celastrus', 15130, 85,22856)
celastrus.update_gpgain(22935,4)
redwood = Trees('Redwood', 22450, 90,22859, growth_time=5)
hardwood = Trees('Mahogny', 15720,55,21480 ,growth_chance = 96, growth_time=4)
calqaut = Trees ('Calquat', 12516,72,5503 ,growth_chance = 90)
all_trees = [fruit, hespori, celastrus, calqaut, hardwood, redwood, regular]


while True:
	day += 1
	for tree in all_trees:
		if day % tree.growth_time == 0:
			daily_exp, daily_cost = tree.grow_patches(cur_level)
			current_exp += daily_exp
			current_cost += daily_cost
			

	if current_exp >= levels[0]:
		cur_level += 1
		day_level_gained.append(day)
		levels.pop(0)

		if cur_level == 99:
			break
		
print(day_level_gained)
print(current_cost)
	



