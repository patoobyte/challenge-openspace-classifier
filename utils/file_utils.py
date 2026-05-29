def load_colleagues(filename: str) -> list:
	"""
	This function prepares the content of the input .txt file to be used by our program.

	Params:
		filename: (str) Name of the file where the list of potential occupants is stored.
	Return:
		(list) Contains all occupants to be placed.
	"""
	# Reads the file and transforms its content into a list of names that our program can use.
	with open(filename) as file:
		file_content = file.read()
	colleagues = file_content.split()
	return colleagues