import os
import textwrap

def help():
	print(textwrap.fill("You are currently using IntelliCare, and intelligent hospital triaging system. The system uses advanced machine learning techniques to determine traige scores based on your assessment of the patient. Don't worry - the system will always ask for your confirmation before the traige score is finalized!"))
	print("There are a number of commands available for you to use:")
	print("new patient: This command will take you through a series of questions about the patient and will generate a triage score")

def new_patient():
	print(textwrap.fill("You will be asked a number of questions about the patient. Answer to the best of your ability. To cancel the new patient operation, type CANCEL at any point."))
	name = input("Name: ")
	age = input("Age: ")
	gender = input("Gender [M\F]: ")
	pregnancy_state = input("Is the patient pregnant? [y/n]: ")
	heart_rate_bpm = input("Heart rate (beats per minute): ")
	breaths_per_minute = input("Breaths per minute: ")
	body_temperature = input("Body temperature: ")
	blood_pressure = input("Blood pressure: ")
	ox_sat = input("Oxygen saturation level: ")
	# Add more here. Qualitative things?

	print("\nInformation collected. Computing triage score...")


# Main parser function. Runs in a while loop forever, always asking the user
# for commands and then following up with the appropriate action.
def parse():
	# Clear the terminal screen
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Welcome to IntelliCare!")
	print("Type the 'help' command for a list of common commands.")

	# Loop forever 
	while(True):
		print(" >> ", end='')
		command = input()
		if(command == "new patient"):
			new_patient()
		elif(command == "help"):
			help()