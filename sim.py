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

def sim(hospital, queue)
    # Current simulation time in seconds
    curr_time = 0
    while(not queue.isEmpty()):

        nextPatient = queue.pop()






        curr_time += 1


    end


def allocatePatient(queue, hospital):
    patient = queue.pop()
    if patient.priority > 0.8:
        floor

def makeHospital(floors, beds):
    # Represent hospital as a nested array
    # Outer Array: represent hospital floors
    # Sub-arrays: represent beds in a given floor

    hospital = []
    for i in range(floors):
        hospital.append([])
        for j in range(beds[i]):
            bed_object = Bed(0, 0)
            hospital[i].append(bed_object)

    return hospital


if __name__ == "__main__":
    beds = [100, 100, 100]
    hospital = makeHospital(len(beds), beds)
    patient_queue = buildQueue(filename)

    sim(hospital, patient_queue)
