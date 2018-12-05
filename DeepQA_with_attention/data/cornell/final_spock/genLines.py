MOVIE_ID = "m617"
BASE_LINE = 99999 + 1
BASE_CHAR = 999 + 1

LINE_PREFIX = "L"
CHAR_PREFIX = "u"
LINES_FILE = "output/final.conv"

DELIMITER = " +++$+++ "

def get_min():
    lines_file = "../cornell/movie_lines.txt"
    chars_file = "../cornell/movie_conversations.txt"
    line_file = open(lines_file)
    char_file = open(chars_file)
    lines = []
    for line in line_file:
        lines.append(line.split()[0])
    print("Max Line: ", max(lines))

    chars = []
    for line in char_file:
        chars.extend(line.split('+++$+++')[0:2])

    print("Max Char: ", max(chars))

def get_char_map(lines):
    chars = set()
    for l1, l2 in lines:
        assert(":" in l1 and ":" in l2)
        chars.add(l1[0:l1.find(":")])
        chars.add(l2[0:l2.find(":")])

    ret_chars = {}
    for i, character in enumerate(chars):
        ret_chars[character] = BASE_CHAR + i
    ret_chars
    return ret_chars

def get_lines():
    lines = []
    f = open(LINES_FILE, 'r', encoding = "ISO-8859-1")
    for line in f:
        lines.append(line.split(DELIMITER))
    return lines

def format_line(index, char_name, char_id, line):
    return DELIMITER.join([LINE_PREFIX + str(BASE_LINE + index), CHAR_PREFIX + str(char_id), MOVIE_ID, char_name, line.strip()])

def format_conv(char1, char2, index, chars):
    return DELIMITER.join([CHAR_PREFIX + str(chars[char1]), CHAR_PREFIX + str(chars[char2]), MOVIE_ID, str([LINE_PREFIX + str(BASE_LINE + index), LINE_PREFIX + str(BASE_LINE + index + 1)])])

def get_formatted_lines_chars(lines, chars):
    output_lines = []
    output_conversation = []
    for i in range(len(lines)):
        l1, l2 = map(lambda x: x[x.find(":") + 1:], lines[i])
        char1, char2 = map(lambda x: x[0:x.find(":")], lines[i])
        output_lines.append(format_line(i*2,   char1, chars[char1], l1))
        output_lines.append(format_line(i*2+1, char2, chars[char2], l2))
        output_conversation.append(format_conv(char1, char2, i*2, chars))
    return output_lines, output_conversation

def main():
    lines = get_lines()
    chars = get_char_map(lines)
    lines, conversation = get_formatted_lines_chars(lines, chars)
    with open("character_conversations.txt", 'w+') as conv_file:
        for line in conversation:
            print(line, file=conv_file)
    with open("character_lines.txt", 'w+') as lines_file:
        for line in lines:
            print(line, file=lines_file)

main()
