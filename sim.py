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
    while not queue.is_empty():

        patient, floor, bed = check_4_openings(queue, hospital)

        # Case 1: no patient can be allocated (all beds full)
        # Case 2: patient can be allocated to a specific bed and floor
        if patient != -1:
            floor -= 1
            z_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      # Will be used for calculating performance metrics
            hospital[floor][bed].assign_patient(patient.id, patient.total_time, z_array)


        curr_time += 1




def check_4_openings(queue, hospital):
    # If patient can be allocated, returns patient object
    # Else, returns -1

    popped_patients = []
    while not queue.is_empty():

        next_floor = allocate_patient(queue, hospital)
        next_bed = check_4_beds(next_floor, hospital)
        if next_bed == -1:                              # Bed for this patient not available
            popped_patients.append(queue.pop())
        else:                                           # Bed for this patient available
            # Insert all patients back into the priority queue
            next_patient = queue.pop()                  # This patient can be allocated
            for i in range(len(popped_patients)):
                queue.insert(popped_patients[i])
            return next_patient, next_floor, next_bed

    # Was not able to assign any patient
    # Insert all patients back into priority queue
    for i in range(len(popped_patients)):
        queue.insert(popped_patients[i])

    return -1, 0, 0


def check_4_beds(floor, hospital):
    # Function: will return index of the next available
    #           bed at the indicated floor
    floor -= 1
    for i in range(len(hospital[floor])):
        if hospital[floor][i].occupancy:
            # Index of the next available bed
            return i

    # If no beds are available, return -1
    return -1


def allocate_patient(queue, hospital):
    patient = queue.pop()
    if patient.priority == 1:
        queue.insert(patient_queue)
        return 3                                            # Assign patient to floor 3, ICU
    elif patient.priority == 2 or patient.priority == 3:
        queue.insert(patient_queue)
        return 2                                            # Assign patient to floor 2, Moderate
    else:
        queue.insert(patient_queue)
        return 1                                            # Assign patient to floor 1, Low Priority

def make_hospital(floors, beds):
    # Represent hospital as a nested array
    # Outer Array: represent hospital floors
    # Sub-arrays: represent beds in a given floor

    hospital = []
    for i in range(floors):
        hospital.append([])
        for j in range(beds[i]):
            bed_object = Bed(0, i, j)
            hospital[i].append(bed_object)

    return hospital


if __name__ == "__main__":
    beds = [100, 100, 100]
    hospital = make_hospital(len(beds), beds)
    patient_queue = build_queue(filename)

    sim(hospital, patient_queue)

