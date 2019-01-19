# A patient class. Use this to represent a patient in the system. Attributes
# added or deleted in the future.
class Patient:
	def __init__(self, id, name, priority, total_time, bed_number, wait_time, age, gender, pregnancy_state, heart_rate_bpm, breaths_per_minute, body_temp, blood_pressure, ox_sat):
		self.id = id
		self.name = name
		self.priority = priority
		self.total_time = total_time
		self.bed_number = bed_number
		self.wait_time = wait_time
		self.age = age
		self.gender = gender
		self.pregnancy_state = pregnancy_state
		self.heart_rate_bpm = heart_rate_bpm
		self.breaths_per_minute = breaths_per_minute
		self.body_temp = body_temp
		self.blood_pressure = blood_pressure
		self.ox_sat = ox_sat


class Bed:
	occupancy = False
	patient = None
	turnover_time = 0
	maintenance_time = 0

	def __init__(self, doctor_id, floor, bed_id):
		self.doctor_id = doctor_id
		self.floor = floor
		self.bed_id = bed_id

	def assign_patient(self, patient, metadata):
		print(patient.name + " (patient " + str(patient.id) + ") has been assigned to bed " + str(self.bed_id))

		metadata[patient.priority - 1] += patient.wait_time
		metadata[4 + patient.priority] += 1
		metadata[10] = max(metadata[10], patient.wait_time)

		metadata[11 + self.floor] += self.turnover_time
		metadata[14+self.floor] += 1
		self.occupancy = True
		self.patient = patient
		self.turnover_time = -1
		self.maintenance_time = 20



	def update_bed(self):
		if self.occupancy:
			self.patient.total_time -= 1

		if not self.occupancy:
			self.turnover_time += 1
			if self.maintenance_time != 0:
				self.maintenance_time -= 1

		if self.patient.total_time == 0:
			self.occupancy = False
			print(self.patient.name + " has been released from the hospital, bed " + str(self.bed_id) + " is now free")
			self.patient = None


class PatientQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def is_empty(self):
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