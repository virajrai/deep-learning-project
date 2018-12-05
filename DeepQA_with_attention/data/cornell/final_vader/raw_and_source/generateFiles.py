import numpy as np 


def get_lines(fileName):

	inFile = open(fileName)
	lines = [line.strip() for line in inFile.readlines()]
	inFile.close()
	return lines


def processLine(line, i, key, charName):

	lineNumber = "L"+str(i)
	delimiter = " +++$+++ "
	newLine = '"'.join(line.split('"')[5:])
	#I choose m617 since appending to end of cornell set which ends at m616
	output = lineNumber + delimiter + key + delimiter + "m617" + delimiter + charName + delimiter + '"' + newLine 
	return output




#Need to manually keep track of movie breaks


def createVaderConversations():

	inFileConversations = open("star-wars-movie-conversations_600.txt")
	convoLines = inFileConversations.readlines()
	inFileConversations.close()
	outFile = open("star-wars-vader-conversations_600.txt", "w")
	delimiter = " +++$+++ "
	for line in convoLines:
		char1 = line.split(delimiter)[0]
		char2 = line.split(delimiter)[1]
		if char1 == 'u3' or char2 == 'u3':
			outFile.write(line)
	outFile.close()



def createLines():

	runningLineNumber = 0
	outFile = open("star-wars-movie-lines_600.txt", "w")
	for k in range(600):
		
		runningLineNumber -= 1
		ep4Lines = get_lines("SW_EpisodeIV.txt")[1:]
		ep5Lines = get_lines("SW_EpisodeV.txt")[1:]
		ep6Lines = get_lines("SW_EpisodeVI.txt")[1:]
		#print("Number of Lines in Episode 4 " + str(len(ep4Lines)))
		#print("Number of Lines in Episode 5 " + str(len(ep5Lines)))
		#print("Number of Lines in Episode 6 " + str(len(ep6Lines)))

		charNumber = 0
		characterIDDic = {}
		characterLines = {}
		episodeLines = []
		episodeLines.extend(ep4Lines)
		episodeLines.extend(ep5Lines)
		episodeLines.extend(ep6Lines)
		#print("Total Number of Lines " + str(len(episodeLines)))
		prevChar = None
		curLine = ""
		lineNumber = 0
		for i,line in enumerate(episodeLines):

			if lineNumber == 846:
				lineNumber += 1
				runningLineNumber += 1
			
			char = line.split('"')[3]
			if char == prevChar:
				newLine = " ".join(line.split()[2:])
				newLine = newLine[1:]
				curLine = curLine[:-1]
				curLine += " "
				curLine += newLine
			else:
				outFile.write(curLine)
				if i != 0:
					outFile.write("\n")

				if char not in characterIDDic:
					key = "u"+str(charNumber)
					charNumber += 1
					characterIDDic[char] = key
				else:
					key = characterIDDic[char]

				prevChar = char
				curLine = processLine(line, runningLineNumber+700000, key, char)
				lineNumber += 1
				runningLineNumber += 1

	
	outFile.close()


def createConversations():

	movieLinesFile= open("star-wars-movie-lines_600.txt")
	movieLines = movieLinesFile.readlines()
	movieLinesFile.close()
	outFile = open("star-wars-movie-conversations_600.txt", "w")
	delimiter = " +++$+++ "
	#print(movieLines[0])
	line0 = movieLines[0].split(" +++$+++ ")
	char1 = line0[3]
	line1 = movieLines[1].split(" +++$+++ ")
	char2 = line1[3]
	curCharSet = [char1, char2]
	outString = line0[1] + delimiter + line1[1] + delimiter + "m617" + delimiter
	lineList = [line0[0], line1[0]]
	i = 2
	while i < len(movieLines)-1:
		if i == 2122:
			print(movieLines[i])
		if i%2122 == 0:
			print(i)
			#outString += str(lineList)
			#outFile.write(outString)
			#outFile.write("\n")
			line0 = movieLines[i].split(" +++$+++ ")
			char1 = line0[3]
			line1 = movieLines[i+1].split(" +++$+++ ")
			char2 = line1[3]
			curCharSet = [char1, char2]
			outString = line0[1] + delimiter + line1[1] + delimiter + "m617" + delimiter
			lineList = [line0[0], line1[0]]
			i += 2
		line = movieLines[i].split(delimiter)
		if line[3] in curCharSet:
			if len(lineList) > 6:
				tempOutString = outString
				outString += str(lineList[:-1])
				outFile.write(outString)
				outFile.write("\n")
				outString = tempOutString
				lineList = [lineList[-1], line[0]]
			else:
				lineList.append(line[0])
			i += 1
		else:
			if (i+1)%2122 == 0:
				print(i)
				outString += str(lineList)
				outFile.write(outString)
				outFile.write("\n")
				i += 1
			else:
				outString += str(lineList)
				outFile.write(outString)
				outFile.write("\n")
				nextLine = movieLines[i+1].split(delimiter)
				curCharSet = [line[3], nextLine[3]]
				outString = line[1] + delimiter + nextLine[1] + delimiter + "m617" + delimiter
				lineList = [line[0], nextLine[0]]
				i += 2
	outFile.close()

#createLines()
#createConversations()
createVaderConversations()