import re  # regex

# my_text = (
#     "This is python3 and it is easy to learn. Python2 is outdated. myemail@gmail.com"
# )
# my_pattern = "is"

# Patterns
# [a-d] matches the letters a-d
# \w matches any letter, digit or underscore
# \w\w\w matches a 3 character string
# \W matches any character that is not \w
# \d matches any digit
# \d\d\d\d matches 4 digit
# . matches any character except \n
# \. to indicate a .

# print(re.findall(my_pattern, my_text))  # match string, not word

# my_text = "My IP is 172.100.200.108. not 10.10.20.20."
# my_pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"

# print(re.findall(my_pattern, my_text))  # match string, not word

# ^ start of a line
# ^i[ts] starts with it or is
# $ end of a line
# learn$ the line ends with learn
# \b empty string at the beginning or end of a word
# r'\blearn\b' matches the word learn exactly, r = raw string
# r'\Blearn\B' matches the word with extra characters at the beginning and the end
# \t \n \r matches a tab newline and return respectively
# {2} match exactly 2 times the previous character
# {2,4} matches 2 to 4 times the previous character
# {2,} matches 2 or more times the previou character
# + matches 1 or more times the previous character
# * matches 0 or more times the previou character
# ? matches once or non times the previou character

# my_text = "This is a string THIS is another String thiS is the third STRing"
# my_pattern = r"this"
# print(re.findall(my_pattern, my_text, re.I))

# my_text = """This is a multiline string
# This is another line
# This is the third line
# What about this"""
# my_pattern = r"^this"
# print(re.findall(my_pattern, my_text, re.I | re.M)) #re.I case insentive, re.M search every line in the multiline string

# my_text = (
#     "This is for python. There are python2 and python3 now. Soon there will be python4"
# )
# my_pattern = r"\bpython[23]?\b"
# match_obj = re.search(my_pattern, my_text)  # find only the first match, does not work with multiline string
# if match_obj:
#     print(match_obj)
#     print("Match from pattern: ", match_obj.group())
#     print("Starting index: ", match_obj.start())
#     print("Ending index: ", match_obj.end() - 1)
#     print("Length: ", match_obj.end() - match_obj.start())
# else:
#     print('No match found.')

# my_text = (
#     "This is for python. There are python2 and python3 now. Soon there will be python4"
# )
# my_pattern = r"\bpython[23]?\b"
# # print(re.findall(my_pattern, my_text))
# print(re.finditer(my_pattern, my_text))
# for obj in re.finditer(my_pattern, my_text):
#     print(
#         f"The match is: {obj.group()}, starting index: {obj.start()}, ending index: {obj.end()}"
#     )


my_text = (
    "This is for python. There are python2 and python3 now. Soon there will be python4"
)
my_pattern = r"\bpython[23]?\b"
newList = re.split(my_pattern, my_text, maxsplit=1)  # maxsplit: how many times to split
print(newList)
newList2 = re.sub(
    my_pattern, "java", my_text, count=2
)  # count: how many times to replace
print(newList2)
newList3 = re.subn(
    my_pattern, "java", my_text
)  # subn: returns the number of times sub happens
print(newList3)
