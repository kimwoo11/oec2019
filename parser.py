import os
import textwrap
from use_model import use_model
from util import *


def help():
    print(textwrap.fill(
        "You are currently using IntelliCare, and intelligent hospital triaging system. "
        "The system uses advanced machine learning techniques to determine traige scores "
        "based on your assessment of the patient. Don't worry - the system will always ask "
        "for your confirmation before the traige score is finalized!"))
    print("There are a number of commands available for you to use:")
    print(textwrap.fill(
        "new patient: This command will take you through a series of questions about the "
        "patient and will generate a triage score"))


def new_patient(patient_queue):
    print(textwrap.fill(
        "You will be asked a number of questions about the patient. Answer to the best of your ability. "
        " cancel the new patient operation, type QUIT at any point."))
    name = input("Name: ")
    if name == "QUIT":
        return
    age = input("Age: ")
    if age == "QUIT":
        return

    gender = input("Gender [m/f]: ")
    if gender == "QUIT":
        return
    if gender != 'm' and gender != 'f':
        print("Invalid input. Patient not registered.")
        return
    if gender == 'm':
        gender = 1
    elif gender == 'f':
        gender = 0

    pregnancy_state = str(input("Is the patient pregnant? [y/n]: "))
    if pregnancy_state == "QUIT":
        return
    if pregnancy_state != 'y' and pregnancy_state != 'n':
        print("Invalid input. Patient not registered.")
        return
    if pregnancy_state == 'y':
        pregnancy_state = 1
    elif pregnancy_state == 'n':
        pregnancy_state = 0

    heart_rate_bpm = input("Heart rate (beats per minute): ")
    if heart_rate_bpm == "QUIT":
        return

    breaths_per_minute = input("Breaths per minute: ")
    if breaths_per_minute == "QUIT":
        return

    body_temperature = input("Body temperature: ")
    if body_temperature == "QUIT":
        return

    blood_pressure = input("Blood pressure: ")
    if blood_pressure == "QUIT":
        return

    ox_sat = input("Oxygen saturation level: ")
    if ox_sat == "QUIT":
        return

    # Add more here. Qualitative things?

    patient_list = [int(age), int(gender), pregnancy_state, int(heart_rate_bpm), int(breaths_per_minute),
                    int(body_temperature), int(blood_pressure),
                    int(ox_sat), 0, 0, 0]
    level = use_model(patient_list)
    

    print("\nInformation collected. Computing triage score...")
    print("\nCalculated triage score: {}".format(level))
    level = input("\nWhat triage score would you like to assign to the patient? ")
    print("New patient successfully added.")

    patient = Patient(0, name, level, 0, 0, 0, age, gender, pregnancy_state, heart_rate_bpm, breaths_per_minute,
                      body_temperature, blood_pressure, ox_sat)
    patient_queue.insert(patient)


# Main parser function. Runs in a while loop forever, always asking the user
# for commands and then following up with the appropriate action.
def parse(patient_queue):
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to IntelliCare!\n")
    print("Type the 'help' command for a list of common commands.")
    print("Type 'QUIT' to quit.")

    # Loop forever
    while True:
        print(">> ", end='')
        command = input()
        if command == 'QUIT':
            return
        elif command == "new patient":
            new_patient(patient_queue)
        elif command == "help":
            help()
        else:
            print("Not a valid command. Type 'help' for assistance.")
