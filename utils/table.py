class Seat:
	"""
	Class representing one seat.

	Attributes:
		free: (bool) Availability status of the seat.
		occupant: (str) Name of the person occupying the seat. 
	"""
	free: bool
	occupant: str

	def __init__(self) -> None:
		"""
		Constructor for a seat.
		"""
		# A seat is initialized empty.
		self.free = True
		self.occupant = ""

	def set_occupant(self, occupant: str) -> None:
		"""
		Function that will assign an empty seat to an occupant given in params.

		Params:
			occupant: (str) Name of the person placed at the seat.
		Return: 
			None.
		"""
		# If a seat is available, place an occupant, then sets the seat's status to unavailable. 
		if self.free == True:
			self.occupant = occupant
			self.free = False
	
	def remove_occupant(self) -> str:
		"""
		Function that will free an occupied seat.

		Return:
			(str) Name of the occupant the function removed.
		"""
		# If a seat is occupied, store the occupant's name, frees the seat and returns the stored name.
		if self.free == False:
			previous_occupant = self.occupant
			self.occupant = None
			self.free = True
			return f"Previous occupant: {previous_occupant}"

	def __str__(self) -> str:
		""" 
		Returns a readable str instead of the object's id. 

		Return:
			(str) A readable representation of the seat object.
		"""
		return f"An empty seat.\n"

class Table:
	"""
	Class representing one table, which contain seat(s).

	Attributes:
		capacity: (int) Number of seats per table.
		table_number: (int) Number of the table.
		seats: (list) List of seats for the table.
	"""
	capacity: int
	table_number: int
	seats: list

	def __init__(self, capacity: int, table_number: int) -> None:
		"""
		Constructor for a table.

		Params:
			capacity: (int) Number of seats per table.
			table_number: (int) Table's identifying number.
		Return: 
			None.
		"""
		self.capacity = capacity
		self.seats = [Seat() for _ in range(self.capacity)]
		self.table_number = table_number

	def has_free_spot(self) -> bool:
		"""
		Checks if the table has an available seat.

		Return:
			(bool) Availability status of the seat.
		"""
		# If there is a free seat at the table, returns True.
		for seat in self.seats:
			if seat.free == True:
				return True
		return False
		
	def assign_seat(self, name: str) -> None:
		"""
		Assigns an available seat to a name.

		Params:
			name: (str) Occupant's name.
		Return: 
			None
		"""
		# Loops through the seats of the table and assigns the occupant to the first free one.
		for seat in self.seats:
			if seat.free == True:
				seat.set_occupant(name)
				return
	
	def left_capacity(self) -> int:
		"""
		Calculate the remaining available seats at the table.

		Return: 
			(int) The number of remaining available seats at the table.
		"""
		# Starts by storing the total number of seats at the table in the variable 'left'.
		left = self.capacity
		# Loops through the seats and decrements 'left' by 1 for each unavailable seat.
		for seat in self.seats:
			if seat.free == False:
				left -= 1
		return left
	
	def __str__(self) -> str:
		"""
		Returns a readable str instead of the object's id.

		Return: 
			(str) A readable representation of the table object.
		"""
		return f"Table #{self.table_number} with {self.capacity} available seats.\n"