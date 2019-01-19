# This is the main file. Run this to start the application.
from util import *
from parser import *
from sim import *

if __name__ == '__main__':


	beds = [100, 100, 100]
	hospital = make_hospital(len(beds), beds)
	patient_queue = build_queue('data.txt')

	parse(patient_queue)

	curr_time = 0  # Minute-by-minute timestamp of the simulation
	metadata = []  # Metadata will store the simulations performance metrics
	for i in range(18):
		metadata.append(0)

	curr_time = sim(hospital, patient_queue, metadata, curr_time)
	final_statistics(metadata, hospital, curr_time)