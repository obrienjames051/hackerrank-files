import re

text = [str(input()) for _ in range(int(input()))] # takes n lines of text as an input

for i in text: # uses re.sub to replace && and || in the text
    i = re.sub(r"(?<= )&&(?= )", " and ", i) # (?<= ) means ensure there is space before
    i = re.sub(r"(?<= )\|\|(?= )", " or ", i) # (?= ) means ensure there is space after
    print(i)