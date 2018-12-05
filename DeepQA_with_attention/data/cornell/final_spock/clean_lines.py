import re
DELIMITER = "+++$+++"

remove_braces_regex = re.compile(r"[\(\[].*?[\)\]]")

remove_braces = lambda x: remove_braces_regex.sub("", x)

def get_conv(file_num):
	FILE = str(file_num) + ".htm"

	lines = []
	cont = False

	for line in open('pages/' + FILE, 'r', encoding = "ISO-8859-1"):
		lines.append(line.strip())

	characterLines = []
	for i in range(len(lines) - 1):
		line = lines[i]
		if line.replace("<br>", '').startswith("<") or len(line) < 2 or line=="<br>":
			cont=False
			continue
		elif cont:
			characterLines[len(characterLines) - 1] += line.strip("<br>") + " "
		elif line.find(":") != -1:
			characterLines.append(line.strip("<br>") + " ")
		if line.find("<br>") == -1:
			cont=True
		else:
			cont=False

	finalLines = []
	for i in range(1, len(characterLines)):
		line = characterLines[i]
		if line.startswith('SPOCK'):
			finalLines.append((remove_braces(characterLines[i-1].strip()), remove_braces(line.strip())))

	output = []
	with open("output/" + str(file_num) + '.conv', 'w', encoding = "ISO-8859-1") as out:
		for line in finalLines:
			print(line[0], DELIMITER, line[1], file=out)
			output.append(line[0] + " " + DELIMITER + " "+ line[1])
	return output

def main():
	final_out = []
	for i in range(1,80):
		final_out.extend(get_conv(i))

	with open("output/final.conv", 'w',encoding = "ISO-8859-1") as out:
		for line in final_out:
			print(line, file=out)

if __name__ == "__main__":
	main()