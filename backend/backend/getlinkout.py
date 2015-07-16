import fileinput

for line in fileinput.input():
	if isinstance(line, list):
		if len(line) == 9 :
			line.pop(0)

