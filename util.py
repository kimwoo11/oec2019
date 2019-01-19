# A patient class. Use this to represent a patient in the system. Attributes
# added or deleted in the future.
class Patient:
	def __init__(self, id, name, priority, total_time, bed_number, wait_time, age, gender, pregnancy_state, heart_rate_bpm, breaths_per_minute, body_temp, blood_pressure, ox_sat):
		self.id = id
		self.name = name
		self. priority = priority
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