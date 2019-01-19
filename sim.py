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
