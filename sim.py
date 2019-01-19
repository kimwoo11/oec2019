from typing import List, Any

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

def patient_status(patient):
    print("Patient Name: "+ patient.name )
    print("     ID: "+ patient.id)
    print("     Priority: " + patient.priority)
    print("     Age: " + patient.age)
    print("     Gender: " + patient.gender)
    if patient.bed_number == -1 :
        print("     Status: Still Waiting")
        print("     Wait Time: "+ patient.wait_time)

    else:
        print("     Status: In Care")
        print("     Bed ID: "+ patient.bed_number)
        print("     Time Remaining: " + patient.total_time)

def bed_status(bed):
    print("Bed Number: " + bed.bed_id)
    print("     Floor:" + bed.floor)
    print("     Doctor assigned: " + bed.doctor_id)
    if bed.occupancy:
        print("     Status: Occupied")
        print("     Patient: " + bed.patient.name)

    else:
        print("     Status: Unoccupied")
        print("     Maintenance Time Remaining: " + bed.maintenance_time)


def final_statistics(metadata):
    #Patient Wait Time
    print("Average Patient Wait Time")
    print("     total: "+str((metadata[0]+metadata[1]+metadata[2]+metadata[3]+metadata[4])/(metadata[5]+metadata[6]+metadata[7]+metadata[8]+metadata[9])))
    print("     Priority Level 1: "+str((metadata[0])/(metadata[5])) + " min.")
    print("     Priority Level 2: " + str((metadata[1]) / (metadata[6])) + " min.")
    print("     Priority Level 3: " + str((metadata[2]) / (metadata[7])) + " min.")
    print("     Priority Level 4: " + str((metadata[3]) / (metadata[8])) + " min.")
    print("     Priority Level 5: " + str((metadata[4]) / (metadata[9])) + " min.")

    print("Maximum Patient Wait Time: " + str(metadata[10]))
    #Bed turnover
    print("Average Bed Turnover Time")
    print("     total: " + str((metadata[11] + metadata[12] + metadata[13]) / (metadata[14] + metadata[15] + metadata[16])) + " min.")
    print("     Main Floor: " + str((metadata[11]) / (metadata[14])) + " min.")
    print("     Step Down: " + str((metadata[12]) / (metadata[15])) + " min.")
    print("     Intensive Care Unit: " + str((metadata[13]) / (metadata[16])) + " min.")
   
    #Bed Occupancy

    #Queue Size


def sim(hospital, queue)
    # Full simulation, patient to bed allocation based on patient priority
    # given by the machine learning model

    curr_time = 0           # Minute-by-minute timestamp of the simulation
    metadata = []           # Metadata will store the simulations performance metrics
    for i in range(17):
        metadata.append(0)

    while not queue.is_empty():

        patient, floor, bed = check_4_openings(queue, hospital)

        # Case 1: no patient can be allocated (all beds full)
        # Case 2: patient can be allocated to a specific bed and floor
        if patient != -1:
            floor -= 1
            # Will be used for calculating performance metrics
            hospital[floor][bed].assign_patient(patient, metadata)


        for i in range(len(queue)):
            queue[i].wait_time += 1
            queue[i].priority = wait_to_priority(queue.wait_time, queue[i].priority)

        # Update timestamps for every bed in the hospital
        for i in range(len(hospital)):
            for j in range(len(hospital[i])):
                hospital[i][j].update_bed()

        curr_time += 1


def check_4_openings(queue, hospital):
    # If patient can be allocated, returns patient object
    # Else, returns -1

    popped_patients = []
    while not queue.is_empty():

        # Obtain the next patients floor and potential bed
        next_floor = find_patient_floor(queue, hospital)
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


def find_patient_floor(queue, hospital):
    # Assigns patient to a floor based on their priority

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


def wait_to_priority(wait, priority):
    if priority == 1:
        return priority
    elif priority == 2 and wait >= 60:
        return 1
    elif priority == 3 and wait >= 120:
        return 2
    elif priority == 4 and wait >= 240:
        return 3
    elif priority == 5 and wait >= 480:
        return 4



if __name__ == "__main__":
    beds = [100, 100, 100]
    hospital = make_hospital(len(beds), beds)
    patient_queue = build_queue(filename)
    sim(hospital, patient_queue)

