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