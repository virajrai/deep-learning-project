import requests
import bs4
import re
from bs4 import BeautifulSoup
# from soupselect import select

DELIMITER = " +++$+++ "
remove_braces_regex = re.compile(r"[\(\[<].*?[>\)\]]")
remove_braces = lambda x: remove_braces_regex.sub("", x)


def get_page(i):
    quote_page = "http://transcripts.foreverdreaming.org/viewtopic.php?f=177&t=%d" % i
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    data = requests.get(quote_page, headers=headers).text
    soup = BeautifulSoup(data, features="html.parser")
    trans = soup.findAll("div", {'class': 'postbody'})[0].findAll('p')
    lines = []
    for item in trans:
        line = ""
        for stuff in item.childGenerator():
            line += remove_braces(str(stuff))
        if line != "" and not line.startswith("ad"):
            lines.append(line)
    return lines

def clean_lines(lines, file_num):
    char_lines = []
    for line in lines:
        if line.find(":") == -1 or line.find("<") != -1:
            continue
        char_lines.append(str(line))

    final_lines = []
    for i in range(1, len(char_lines)):
        line = char_lines[i]
        if line.startswith("Barney"):
            final_lines.append((remove_braces(char_lines[i - 1].strip()), remove_braces(line.strip())))

    output = []
    with open("output/" + str(file_num) + '.conv', 'w', encoding="ISO-8859-1") as out:
        for line in final_lines:
            print(line[0], DELIMITER, line[1], file=out)
            output.append(line[0] + " " + DELIMITER + " " + line[1])
    return output

def main():
    # 11508 11637
    r = range(11508, 11593)
    all_lines = []
    for num in r:
        try:
            page = get_page(num)
            lines = clean_lines(page, num)
            all_lines.extend(lines)
            print("\rDownloading page %d of %d"% (num-11507, 11593-11507), end="")
        except:
            print("ERROR in file: %d" % num)
            continue
    print()
    with open("output/final.conv", 'w', encoding="ISO-8859-1") as out:
        for line in all_lines:
            print(line, file=out)

main()
