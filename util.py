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

# The bed class represents a given hospital bed. Attributes represent the status of the bed, the current patient
# occupying the bed, and various timers for later statistical analyses


class Bed:

	# Initializing the bed as empty, and initializing all timers to zero

	occupancy = False
	patient = None
	turnover_time = 0
	maintenance_time = 0
	occupied_time = 0
	empty_time = 0
	occupancy_ratio = 0.0

	# Constructor function

	def __init__(self, doctor_id, floor, bed_id):
		self.doctor_id = doctor_id
		self.floor = floor
		self.bed_id = bed_id

	# The assign patient function is called when a new patient is assigned to a given bed

	def assign_patient(self, patient, metadata):
		print(patient.name + " (patient " + str(patient.id) + ") has been assigned to bed " + str(self.bed_id) + " on floor " + str(self.floor))

		# Updates metadata on patient wait time and turnover time

		metadata[patient.priority - 1] += patient.wait_time
		metadata[4 + patient.priority] += 1
		metadata[10] = max(metadata[10], patient.wait_time)

		metadata[11 + self.floor] += self.turnover_time
		metadata[14+self.floor] += 1
		self.occupancy = True
		self.patient = patient
		self.turnover_time = -1
		self.maintenance_time = 10

	# The update bed function is called at every time step to increment various timers for every bed

	def update_bed(self):

		# If the bed is occupied, decrement the patient's required care time and the bed's occupied time

		if self.occupancy:
			self.patient.total_time -= 1
			self.occupied_time += 1

		# If the bed isn't occupied, increment the bed's empty time, its turnover time,
		# and if any maintenance is required, decrement it's maintenance time

		if not self.occupancy:
			self.turnover_time += 1
			self.empty_time += 1
			if self.maintenance_time != 0:
				self.maintenance_time -= 1

		# If the patient has reached his required care time, release him from the hospital and free this bed
		if self.occupancy:
			if self.patient.total_time == 0:
				self.occupancy = False
				print(self.patient.name + " has been released from the hospital, bed " + str(self.bed_id) + " is now free")
				self.patient = None

		# Calculate the occupancy ratio

		if self.empty_time != 0 or self.occupied_time != 0:
			self.occupancy_ratio = self.occupied_time / (self.empty_time + self.occupied_time)


class PatientQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def is_empty(self):
		if len(self.queue) == 0:
			return True
		else:
			return False

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