from utils.openspace import Openspace
from utils.file_utils import load_colleagues

def main() -> None:
	"""
	Entry point for the Openspace Organizer.
	The function takes user input for table setup,
	loads a list of names from a .txt file, 
	organizes them into available seats,
	and displays the result and store it in a .csv file.

	Return: None.
	"""
	input_file = "./new_colleagues.txt"
	output_file = "openspace_plan.csv"
	# Loop that waits for valid user input. Default configuration is 6 tables of 4 seats each.
	while True:
		launch_setup = str(input("Enter 'd' for a default configuration, 'c' for custom: "))
		if launch_setup == 'd':
			table_number = 6
			table_capacity = 4
			break
		elif launch_setup == 'c':
			table_number = int(input("Please enter the number of tables (int only): "))
			table_capacity = int(input("Please enter the number of seats per table (int only): "))
			break
		else:
			print("Please enter 'd' or 'c'.")
	openspace = Openspace(table_number, table_capacity) # Creates an Openspace object.
	colleagues = load_colleagues(input_file) # Loads the file with names to place.
	try: # Tries to place everyone. Ends the program if there are not enough seats.
		openspace.organize(colleagues)
	except ValueError as error:
		try: # If output_file already exists, its content is wiped.
			with open(output_file, "r+") as file:
				file.truncate()
		except FileNotFoundError: # If output_file does not exist, skip.
			pass
		print(f"Error: {error}")
		return
	openspace.display() # Displays the result on terminal.
	openspace.store(output_file) # Store the result in output_file.

# Entry point check : execute the main only if the file is being executed directly.
if __name__ == "__main__":
	main()