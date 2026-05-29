import random
import csv
from utils.table import Table

class Openspace:
	"""
	Class representing one openspace, which contains tables, which contains seats.

	Attributes:
		number_of_tables: (int) number of tables in the openspace.
		table_capacity: (int) number of seats in one table.
		tables: (list) list of tables in the openspace.
		plan: (list) sitting plan of the openspace
	"""
	number_of_tables: int
	table_capacity: int
	tables: list
	plan: list

	def __init__(self, number_of_tables, table_capacity) -> None:
		"""
		Constructor for an openspace.

		Params:
			number_of_tables: (int) Number of tables in the openspace.
			table_capacity: (int) Number of seats per table.
		Return: 
			None.
		"""
		self.number_of_tables = number_of_tables
		self.table_capacity = table_capacity
		# Creates 1 table until we reach number_of_tables and appends it to the list of tables. 
		self.tables = []
		for i in range(number_of_tables):
			table_number = i + 1 # Add 1 to table_number so numbering starts at 1.
			table = Table(table_capacity, table_number)
			self.tables.append(table)
		# Creates a list to store sitting plan
		self.plan = []

	def organize(self, colleagues: list) -> None:
		"""
		This function shuffles the names of potential occupants,
		then assigns them in available seats, thus making the seat assignment random.

		Params:
			colleagues: (list) Names of potential occupants.
		Return:
			None.
		"""
		self.colleagues = colleagues
		# Checks if there is enough seats. Raises an exception if not enough seats.
		if len(colleagues) > self.table_capacity * self.number_of_tables:
			raise ValueError("Not enough seats.")
		# Shuffles the name list
		random.shuffle(colleagues)
		# Sits everyone. 
		# For each name, find a table with a free spot, then assign a free seat from that table.
		for name in colleagues:
			for table in self.tables:
				if table.has_free_spot() == True:
					table.assign_seat(name)
					break
		# Write the sitting plan into self.plan.
		# For each table, stores its sitting plan in a list.
		for table in self.tables:
			table_plan = []
			for seat in table.seats:
				if seat.free == False:
					table_plan.append(seat.occupant)
				else:
					table_plan.append("None")
			# Appends the table plan to the openspace plan, preceeded by the table number.
			self.plan.append({
				"table_number": table.table_number,
				"table_plan": table_plan
			})

	def display(self) -> None:
		"""
		This function displays the seat placement on the terminal.

		Return:
			None.
		"""
		print()
		# Prints openspace configuration.
		print(f"Sitting plan for {len(self.colleagues)} people on {self.number_of_tables} tables of {self.table_capacity}.\n")
		# Loops the tables.
		for table in self.plan:
			# Prints the table number and a separator.
			print(f"Table #{table["table_number"]}")
			print("--------")
			# Loops through the table_plan.
			for seat_number, occupant in enumerate(table["table_plan"], start=1):
				# If there is an occupant, prints the seat number and the name.
				if occupant != "None":
					print(f"Seat {seat_number}: {occupant}")
				else:
					print("Empty seat.")
			print()
	
	def store(self, filename: str) -> None:
		"""
		This function stores the sitting plan in a file called "openspace_plan.txt".

		Params:
			filename: (str) Name of the file where the sitting plan is stored.
		Return:
			None.
		"""
		# Write on the file the openspace configuration followed by the sitting plan.
		with open(filename, "w", newline="", encoding="utf-8") as file:
			writer = csv.writer(file)
			writer.writerow(["table_number", "seat_number", "occupant"])
			for table in self.plan:
				for i, occupant in enumerate(table["table_plan"], start=1):
					writer.writerow([
						table["table_number"],
						i,
						occupant if occupant != "None" else "Empty"
						])

	def __str__(self):
		""" 
		Returns a readable str instead of the object's id. 

		Return:
			(str) A readable representation of the openspace object.
		"""
		return f"Openspace with {self.number_of_tables} tables of {self.table_capacity} seats each."