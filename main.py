# This is the main file. Run this to start the application.
from util import *
from parser import *
from sim import *

if __name__ == '__main__':
	beds = [100, 100, 100]
	hospital = make_hospital(len(beds), beds)
	patient_queue = build_queue('data.txt')
	parse(patient_queue)