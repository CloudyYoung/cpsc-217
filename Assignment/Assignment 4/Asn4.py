##
# @Name Cloudy Young
# @Student Number 
# @Description Build up a food Web by using dictionary and analyze several kinds data
# @Lines 94 code 73 comments 41 blank
# @Note Completion with A+ standard, some outputs have different order from the expected results but data are the same


# import 'sys' library for reading txt file from command line
import sys

# @name format
# @param text
# @return formatted string
# @description [PART-GLOBAL] convert a list into a formatted string
def format(text):
	if len(text) == 1:
		return text[0]
	elif len(text) == 0:
		return "(None)"
	return ", ".join(text[0:-1]) + " and " + text[-1]


# @name readFoodWeb
# @param foodWebName
# @return dictionary of food web
# @description [PART-1] read txt file and convert it into dictionary food web
def readFoodWeb(foodWebName):
	foodWebText = open(foodWebName).read()
	lines = foodWebText.split("\n")

	foodWeb = {}
	for line in lines:
		if line != "":
			relationship = line.split(",")
			predator = relationship.pop(0)
			foodWeb[predator] = relationship
	return foodWeb


# @name predators
# @param foodWeb
# @return a list contains all predators in the food web
# @description [PART-GLOBAL] take all the predators from food web fidctionary and return a new one-dimension list
def predators(foodWeb):
	return list(foodWeb.keys())


# @name preries
# @param foodWeb
# @return all the preries in a one-dimension list
# @description [PART-GLOBAL] take all the preries from food web fidctionary and return a new one-dimension list
def preries(foodWeb):
	return [x for each in list(foodWeb.values()) for x in each]


# @name apexPredators
# @param foodWeb
# @return a list of all apex predators
# @description [PART-2] get all the predators and preries, use predators list minus preries list and the difference of them are the apex predators
def apexPredators(foodWeb):
	return list(set(predators(foodWeb)) - set(preries(foodWeb)))


# @name producers
# @param foodWeb
# @return a list of all producers
# @description [PART-3] get all the predators and preries, use preries list minus predators list and the difference of them are the producers
def producers(foodWeb):
	return list(set(preries(foodWeb)) - set(predators(foodWeb)))


# @name flexiblePredator
# @param foodWeb
# @return a list of all flexible predators
# @description [PART-4] get predators which eat most kinds of other preries
def flexiblePredator(foodWeb):
	# declare return value variable and sort all predators by the amount of occurances in the list
	flexiblePredator = []
	flexibility = sorted(foodWeb, key = lambda x: len(foodWeb[x]), reverse = True)

	# because the first one is always the most one, as long as the following ones have 
	# the same amount, all of them are the most flexible predators
	for each in flexibility:
		if len(foodWeb[flexibility[0]]) <= len(foodWeb[each]):
			flexiblePredator.append(each)
	return flexiblePredator


# @name tastiestPrey
# @param foodWeb
# @return a list of all tastiest preries
# @description [PART-5] get preries which are eaten the most
def tastiestPrey(foodWeb):
	# declare the return value variable and get the maximum amount in the food web
	tastiestPrey = []
	maxCount = preries(foodWeb).count(max(preries(foodWeb), key = preries(foodWeb).count))

	# because we already have the maximum amount, as long as the preries have 
	# the same amount as the maximum amount, all of them are tastiest preries
	for each in preries(foodWeb):
		if preries(foodWeb).count(each) == maxCount:
			tastiestPrey.append(each)

	# remove the repeated names of preries
	tastiestPrey = list(set(tastiestPrey))
	return tastiestPrey


# @name web
# @param animal, height, foodWeb, heightWeb
# @description [PART-6] this is a recursive function for computing the height of animals
def web(animal, height, foodWeb, heightWeb):
		# for each predator in the food web
		for predator in foodWeb:
			# if it exists in other predators' preies list
			if animal in foodWeb[predator]:
				# it continues to increase height
				web(predator, height + 1, foodWeb, heightWeb)

		# if current branch reaches the highest height, 
		# then compare to its recorded height(if not recorded before, will get default height zero), 
		# then will get the global height in the web, record it to the height web variable
		heightWeb[animal] = max(height, heightWeb.get(animal, 0))


# @name readHeightWeb
# @param foodWeb
# @return heightWeb
# @description [PART-6] initial invoke recursive function 'web'
def readHeightWeb(foodWeb):
	# declare height web variable
	heightWeb = {}

	# start from all the producers which all have height of zero
	# so here the order of output will be different from the expected result
	for each in producers(foodWeb):
		web(each, 0, foodWeb, heightWeb)
	return heightWeb


# @name preriesCount
# @param foodWeb, heightWeb, mode
# @return a list of goal animals
# @description [PART-A+] get the three kinds of animals in the food web
def preriesCount(foodWeb, heightWeb, mode):
	ret = []

	# for each predator in the food web
	for predator in foodWeb:

		# declare amount of plant and animal it eats for current predator
		plant, animal = 0, 0

		# for each prey it eats, judge if it is a plant by prey's height(which is zero), 
		# or an animal in the food web
		for prey in foodWeb[predator]:
			if heightWeb[prey] == 0:
				plant += 1
			else:
				animal += 1

		# according to different mode name, using different conditions 
		# to filter out each kind of predator
		if mode == "herbivores" and animal == 0:
			ret.append(predator)
		elif mode == "carnivores" and plant == 0:
			ret.append(predator)
		elif mode == "omnivores" and animal != 0 and plant != 0:
			ret.append(predator)
	return ret


# @name main
# @description [PART-GLOBAL] the main function of whole program
def main():

	# print predators and their preries
	print("Predators and Prey: ")
	foodWeb = readFoodWeb(sys.argv[1])
	for predators in foodWeb:
		print("  " + predators + " eats " + format(foodWeb[predators]))

	# print aplex pred, producers, flexible preds and tastiest preies
	print("\nApex Predators:", format(apexPredators(foodWeb)))
	print("Producers:", format(producers(foodWeb)))
	print("Most Flexible Eaters:", format(flexiblePredator(foodWeb)))
	print("Tastiest:", format(tastiestPrey(foodWeb)))

	# print height web
	print("\nHeights:")
	heightWeb = readHeightWeb(foodWeb)
	for animals in heightWeb:
		print("  " + animals + ": " + str(heightWeb[animals]))

	# print three kinds of animals
	print("\nFor an A+: ")
	print("  Herbivores: " + format(preriesCount(foodWeb, heightWeb, "herbivores")))
	print("  Omnivores: " + format(preriesCount(foodWeb, heightWeb, "omnivores")))
	print("  Carnivores: " + format(preriesCount(foodWeb, heightWeb, "carnivores")))


main()

# the window will not be automatically closed after finish excuting
input("")

