import room
import random

# Class that descibes a dorm.
class Dorm:

	# initializes a Dorm with the size.
	def __init__(self, name, rooms, accessible=False):
		self.name = name
		self.rooms = rooms
		self.accessible = accessible
		self.fitness = self.dorm_fitness()

	# Gets the fitness value of the dorm based on its students.
	def dorm_fitness(self):
		from helpers import n_choose_2
		total = 0
		# Sum all the fitnesses of individual rooms, weighted by
		# number of compatability values in each room, then divide by total
		# number of compatabilities of that dorm to get a weighted average fitness.
		for rm in self.rooms:
			if rm.size > 1:
				total = total + (rm.room_fitness() * n_choose_2(rm.size))

		# Once done, set fitness value so it
		# does not have to be calculated again
		f = (total / (float(self.count_compatabilites())))
		self.fitness = f
		return f

	def count_compatabilites(self):
		from helpers import n_choose_2
		compats = 0
		for rm in self.rooms:
			if rm.size > 1:
				compats = compats + n_choose_2(rm.size)
		return compats

	def count_rooms(self):
		return len(self.rooms)

	def singles(self):
		counter = 0
		for rm in self.rooms:
			if rm.size == 1:
				counter = counter + 1
		return counter

	def count_students(self):
		s = 0
		for rm in self.rooms:
			s = s + rm.size
		return s


def run_tests():
	pass

run_tests()
