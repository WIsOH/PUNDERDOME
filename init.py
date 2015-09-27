def array_from_text_file(filepath):
	with open(filepath) as f:
    	lines = f.readlines()
		return lines
