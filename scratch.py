class PatientQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == []

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def pop(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i].priority > self.queue[max].priority:
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

from util import *


def build_queue(filename):
    patient_queue = PatientQueue()


    # import data from a file
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    lines = [line.rstrip('\n') for line in lines]


    for line in lines:
        line = line.split(",")
        patient_queue.insert(Patient(line[0], line[1], line[2], line[3], -1, 0, line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13]))

    return patient_queue


if __name__ == '__main__':
    patient_queue = build_queue("data.txt")
    print(patient_queue.pop().name)